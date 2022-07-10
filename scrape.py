from bs4 import BeautifulSoup
import requests

source_tashkent=requests.get('https://en.wikipedia.org/wiki/Tashkent').text
soup=BeautifulSoup(source_tashkent, 'lxml')

l=soup.find_all('ul')
descriptions=l[5]
print(descriptions.text)


#Tashkent, mountains - east, Bukhara, Samarkand - south or north, Nukus - west