

from html.parser import HTMLParser
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen

#SQL connection data to connect and save the data in
from config import const
from config import homescrp


root = 'https://yts.mx/browse-movies'

'''
website = f'{root}/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

'''
# Defining Variables

title_names = []
title_link = []
names = []

# Scraping Browse movies URL
i = 1
while i:
    website = homescrp.home_url(root, i)
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    
    count = len(title_names)
    
    all_link=soup.find_all("a", class_ = const.link_str )
    for link in all_link:
        title_link.append(link.get("href"))

    all_names = soup.find_all("a", class_= const.name_str)
    for name in all_names:
        title_names.append(name.string)
    
    for urll in title_link:
        names.append(urll.split("/movies/",1)[1]) 
    
    for numb in range(len(title_names)): 
        if title_names[numb] == None:
            title_names[numb] = names[numb]
    i+=1
    
    if count == len(title_names):
        break

links = title_link
zipped = list(zip(title_names, title_link))
c = 0
for i in zipped:
    c+=1
    print(c, i)



