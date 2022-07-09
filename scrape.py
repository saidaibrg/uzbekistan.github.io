from bs4 import BeautifulSoup
import requests

source=requests.get('https://en.wikipedia.org/wiki/Kalyan_Minaret').text
soup=BeautifulSoup(source, 'lxml')

tables=soup.find('table')
sight_name=tables.find('a',title='Bukhara').text

sight_name=tables.find('a',title='Bukhara Region').text
print(sight_name)

#ToDO get the information abstract from the Kalyan minaret