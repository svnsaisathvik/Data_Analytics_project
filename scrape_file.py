import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.robotparser import RobotFileParser  # Added for respecting robots.txt

# Function to scrape IMDb movie data
def scrape_imdb(url):
    # Create and open a CSV file for writing
    with open('imdb_top_1000_movies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Poster_Link', 'Series_Title', 'Released_Year', 'Certificate',
                         'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score',
                         'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross'])

        # Respect robots.txt guidelines
        robots_url = 'https://www.imdb.com/robots.txt'
        robots = RobotFileParser()
        robots.set_url(robots_url)
        robots.read()

        # Loop through multiple pages (dynamically based on pagination)
        page_num = 1
        while True:
            page_url = f"{url}&start={10 * (page_num - 1)}"

            # Check robots.txt before making requests
            if not robots.can_fetch("*", page_url):
                print(f"Scraping stopped at page {page_num} due to robots.txt restrictions.")
                break

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            }

            response = requests.get(page_url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find the pagination element (adapt to IMDb's structure)
                pagination = soup.find('div', class_='desc')  # Adjust selector as needed

                # Check if there's a next page link
                next_page_link = None
                if pagination:
                    next_page_link = pagination.find('a', text='Next')

                # Extract data for each movie on the current page
                movies = soup.find_all('div', class_='lister-item mode-advanced')
                for movie in movies:
                    try:
                        # Extract data with improved selectors (adapt as needed)
                        poster_link = movie.find('img')['src'] if movie.find('img') else ''
                        series_title = movie.find('h3', class_='lister-item-header').a.text
                        released_year = movie.find('span', class_='lister-item-year').text.strip('()')
                        certificate = movie.find('span', class_='certificate').text if movie.find('span', class_='certificate') else ''
                        runtime = movie.find('span', class_='runtime').text if movie.find('span', class_='runtime') else ''
                        genre = movie.find('span', class_='genre').text.strip()
                        imdb_rating = movie.find('div', class_='ratings-imdb-rating').strong.text
                        overview = movie.find('p', class_='text-muted').text.strip()
                        meta_score = movie.find('span', class_='metascore').text.strip() if movie.find('span', class_='metascore') else ''
                        director = movie.find('p', class_='').find('a').text
                        stars = [star.text for star in movie.find_all('p')[2].find_all('a')]
                        no_of_votes = movie.find('p', class_='sort-num_votes-visible').find_all('span')[1].text
                        gross = movie.find('p', class_='sort-num_votes-visible').find_all('span')[-1].text if movie.find('p', class_='sort-num_votes-visible').find_all('span')[-1].text != 'Gross: ' else ''

                        # Write the data to the CSV file
                        writer.writerow([poster_link, series_title, released_year, certificate,
                                         runtime, genre, imdb_rating, overview, meta_score,
                                         director, *stars, no_of_votes, gross])
                    except Exception as e:
                        print(f"An error occurred while scraping movie: {e}")
                        continue

                # Move to the next page if available
                if next_page_link:
                    page_num += 1
                else:
                    print("Scraping completed.")
                    break

                # Add a small delay to avoid overwhelming the server
                time.sleep(1)
                
            else:
                print(f"Failed to retrieve webpage for page {page_num}")
                break

    print("Data saved to 'imdb_top_1000_movies.csv'")

# URL of the IMDb "Top Rated Movies" page
url = 'https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv'

# Call the function to scrape IMDb movie data
scrape_imdb(url)


