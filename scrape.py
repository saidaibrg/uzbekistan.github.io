from bs4 import BeautifulSoup
import requests

#RECEIVING END
with open('index.html') as html_file:
    soup_receive = BeautifulSoup(html_file,"html.parser")

images=soup_receive.find_all("a", {"class": "item"})
for image in images:
    print(image["data-caption"])


#SENDING END
source_tashkent=requests.get('https://en.wikipedia.org/wiki/Tashkent').text
soup=BeautifulSoup(source_tashkent, 'lxml')

lst=soup.find_all('ul')
descriptions=lst[5]
#print(descriptions.text)

#The full descriptions of the Eastern Tashkent monuments


#Tashkent, mountains - east, Bukhara, Samarkand - south or north, Nukus - west