import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('universidades.db')
cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS universidades (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, url TEXT)")

def insert_data(name, url):
    cursor.execute("INSERT INTO universidades (name, url) VALUES (?, ?)", (name, url))
    conn.commit()

def get_data():
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.example'
    }
    r = requests.get('https://www.classcentral.com/universities',headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    universidades = soup.find('ul',attrs={"class":"bg-white border-gray-light border-all radius-small list-no-style margin-top-xsmall"}).find_all('li')
    for universidad in universidades:
        tag_a = universidad.find('a')
        url = "https://www.classcentral.com" + tag_a['href']
        name = tag_a.find('span',attrs={"class":"margin-right-xsmall"}).text
        break
    print(len(universidades))

if __name__ == "__main__":
    create_table()
