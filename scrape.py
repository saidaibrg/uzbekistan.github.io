from bs4 import BeautifulSoup
import requests


#East:
#The full descriptions of the Eastern Tashkent monuments
source_tash=requests.get('https://en.wikipedia.org/wiki/Tashkent').text
soup_tash=BeautifulSoup(source_tash, 'lxml')

lst1=soup_tash.find_all('ul')
sights_tash=lst1[5]
sights_tash_list=sights_tash.findChildren('li',recrusive=False)
for each_sight_tash in sights_tash_list:
    print(each_sight_tash.text)
    print("\n\n\n\n")

#West
#Nukus
source_tash=requests.get('https://en.wikipedia.org/wiki/Tashkent').text
soup_tash=BeautifulSoup(source_tash, 'lxml')

lst1=soup_tash.find_all('ul')
sights_tash=lst1[5]
sights_tash_list=sights_tash.findChildren('li',recrusive=False)
for each_sight_tash in sights_tash_list:
    print(each_sight_tash.text)
    print("\n\n\n\n")





#Tashkent, mountains - east, Bukhara, Samarkand - south or north, Nukus - west
