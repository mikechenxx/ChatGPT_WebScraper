import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=RXCW2ZQVWBZ9DMK1EVRE&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_3"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movies = []

for movie in soup.select('tbody.lister-list tr'):
    title = movie.find('td', class_='titleColumn').find('a').text.strip()
    year = movie.find('td', class_='titleColumn').find('span', class_='secondaryInfo').text.strip('()')
    rating = movie.find('td', class_='ratingColumn imdbRating').find('strong').text.strip()
    movies.append((title, year, rating))

for movie in movies:
    print(f"{movie[0]} ({movie[1]}) - {movie[2]}")

with open('250_top_rated_movies.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Year', 'Rating'])
    writer.writerows(movies)