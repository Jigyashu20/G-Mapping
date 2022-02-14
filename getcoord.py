import requests
from bs4 import BeautifulSoup

def find_links(i):
    url = f"https://www.google.com/search?q=longitude+and+latitude+coordinates+of+{i}"
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    # coor = soup.find('div', {'class': 'Z0LcW'})
    coor = soup.find('div', {'class': 'main'})
    return soup.text
