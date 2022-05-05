#Scraping in Every Movie Link
import webscrap as ws
from bs4 import BeautifulSoup
import requests

title_name = []
release_date = []
ratings = []
genre_ = []
director = []
cast = []
download_link_1 = []

for link in ws.links:
    try:
        website = link
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
            
        name = soup.find("h1", itemprop ='name')
        title_name.append(name.string)

        date = soup.find("h2")
        release_date.append(date.string)

        genre = soup.find("h3")
        genre_.append(genre.string)

        rating = soup.find("span", itemprop = 'ratingValue')
        ratings.append(rating.string)

        download_link = soup.find("p", class_ = "hidden-xs hidden-sm")
        dlink = download_link.find("a")
        download_link_1.append(dlink.get("href"))
        
    except (IOError, AttributeError):
        pass
  
zipped2 = list(zip(title_name, release_date, genre_, ratings, download_link_1))
cc = 0
for i in zipped2:
    cc+=1
    print(cc, i)