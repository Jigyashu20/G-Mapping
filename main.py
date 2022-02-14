import requests
from bs4 import BeautifulSoup


def find_coordinates(i):
    b = i[:len(i)-1]
    url = f"https://en.wikipedia.org/wiki/{b}"
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    coor = soup.find('span', {'class': 'geo-dms'})
    return {b: coor.text}


def find_links(i):
    b = i[:len(i)-1]
    url = f"https://en.wikipedia.org/wiki/{b}"
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    coor = soup.find('div', {'id': 'mw-content-text'})
    return coor.find_all('a')

f = open("project.txt", "r")
titles = f.readlines()
dictionary = {}
for i in titles:
    dictionary.update(find_coordinates(i))
for k, l in dictionary.items():
    print(k, l)



for i in titles:
    lis=list(find_links(i))
    
for j in lis:
    print(j.get('href'))
f.close()