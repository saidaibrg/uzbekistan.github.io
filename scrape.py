from bs4 import BeautifulSoup
import requests

source=requests.get('https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Uzbekistan').text
soup=BeautifulSoup(source, 'lxml')

tables=soup.find('table')
sight=tables.find('a',title='Bukhara Region')

print(sight.prettify())