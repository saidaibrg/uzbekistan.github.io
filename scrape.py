from bs4 import BeautifulSoup
import requests

# Tashkent Sights Scraping
source_tash=requests.get('https://en.wikipedia.org/wiki/Tashkent').text
soup_tash=BeautifulSoup(source_tash, 'lxml')

lst1=soup_tash.find_all('ul')
sights_tash=lst1[5]
sights_tash_list=sights_tash.findChildren('li',recrusive=False)
for each_sight_tash in sights_tash_list:
    print(each_sight_tash.text)
    print("\n\n\n\n")

# Bukhara Sights Scraping
source_bukh=requests.get('https://en.wikipedia.org/wiki/Bukhara').text
soup_bukh=BeautifulSoup(source_bukh, 'lxml')
lst1=soup_bukh.find_all('ul')
sights_bukh=lst1[5]
sights_bukh_list=sights_bukh.findChildren('li',recrusive=False)
for each_sight_bukh in sights_bukh_list:
    print(each_sight_bukh.text)
    print("\n\n\n\n")
