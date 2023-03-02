import requests
from bs4 import BeautifulSoup
from lxml import etree

def get_full_data_down(soup, li_xpath):
    list_elements = []
    elements = soup.find('li',attrs={"class":li_xpath}).find('ul').find_all('li')
    for ele in elements:
        a = ele.find('a')
        data = {
            "url": "https://www.classcentral.com"+a['href'],
            "name": a.find('strong',attrs={"class":"margin-left-xsmall fill-space"}).text,
            "img": a.find('img')["src"]
        }
        list_elements.append(data)
        
    return list_elements

def get_data_down(soup):
    down = soup.find('ul',attrs={"class":"list-no-style row large-up-nowrap"})
    universities = get_full_data_down(down,"border-box width-100 large-up-width-3-7 padding-horz-small relative")
    pass

def get_data():
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.example'
    }
    r = requests.get('https://www.classcentral.com/',headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data_down(soup)
get_data()