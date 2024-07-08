
# IMDb Movie Analysis: Predictions and Conclusions
Here we analyse the top movies dataset from IMDb data base and arrive to the possible predictions and conclusions.

## Introduction

In this Dashboard we are having 3 types of Analysis






-  **Genre Analysis(Home page):** Here we are analysing all the genres with parameters such as Revenue By Genre,Rating By Genre,Meta_Score By Genre,No_of_votes,Certificates used the most and the least by charts 
- **Movie Analysis(Second Page):** The Movie analysis has the imdb rating graph compared to all the movies in the Genre,Revenue of the movie compared to other movies in the Genre,No_of_votes of movie with all other genres,Meta Score toanalyse the movies performance.
- **Actor Analysis(Third page):** This page consists of the genres the actors has worked and the movies to select in which the present actor has worked.
- **Predictions And Conclusions:** Here we predicted the best Actor-Director combos using different parameters.The best combo movie to get better IMDb rating,Best Combo movie to get better Meta_Score and Best Combo movie to get a good gross revenue.And finally considering all these parameters(IMDb rating,Meta_Score) and gives the overall best Actor-Director Combo.


## Demo
For better understanding of the Dashboard
 - [Demo video Link](https://www.youtube.com/watch?v=UQvFMOZYDh0&ab_channel=JaswantprabhasJupalli)


## Installation
- you require powerBi desktop application to make or run this dashboard form microsoft store.
- you also require numpy and pandas to be instakked
```bash
    pip install numpy
    pip install pandas
```
## Used libraries for scraping the data
```bash
    import numpy as np
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import csv
    from urllib.robotparser import RobotFileParser
```

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory and open IMDB_top1000_final_final.pbix file in powerBi desktop and then you can use it as shown as in demo video link.


## How is it useful to the **End Users**
- **For identifying Trend changes:** Trend Analysis-Producers and Directors with the released year filter can analyse the various trends in different decades and years and can know the type in which people are interested most recently.

- **Film Industry Decision Making:** Industry professionals such as filmmakers, producers, casting directors, and investors can use the IMDb dashboard to make decisions about casting actors and hiring directors for upcoming projects. By leveraging analytics, they can identify individuals likely to deliver high-performance works, thereby increasing the chances of commercial success and critical acclaim.

- **Actor Analysis:** Producers can see the actor's performance in different movies and the revews he/she is getting while acting in different genres and selecting the genre where they have high chances of doing good.

- **Talent Management**: Talent agencies and managers can utilize the dashboard to assess the future success of their clients (actors and directors). This information can aid in strategic career planning identifying opportunities that align with their clients strengths and aspirations
## Did you Find any bug in this project??
If you find any bug in this project then you can post that bug in the issues section in GitHub itself

## Issues we are currently working with:
- Live scraping of the data from Imdb database.




## 🔗 Contributors
- **JUPALLI PRABHAS:** jupalli.jaswant@iiitb.ac.in
- **Sudhir KH:** Kh.Sudhir@iiitb.ac.in
- **SVN SAI SATHVIK:** SVN.Sathvik@iiitb.ac.in
