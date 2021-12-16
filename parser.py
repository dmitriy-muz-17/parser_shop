import requests
import sqlite3
from bs4 import BeautifulSoup

url = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&country.import.usa.not=-1&price.USD.lte=20000&price.currency=1&gearbox.id[1]=2&gearbox.id[2]=3&gearbox.id[3]=4&gearbox.id[4]=5&fuel.id[5]=6&abroad.not=0&custom.not=1&page=0&size=12'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
price = soup.find_all('span', class_='bold green size22')
name = soup.find_all('span', class_='blue bold')
url = soup.find('a', class_='address').get('href')

for i in url:
    print(i)
#print(type(price))

db = sqlite3.connect('archive.db')
sql = db.cursor()

#sql.execute("DROP TABLE cars")
#db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS cars (
    name TEXT,
    url TEXT,
    price TEXT
)""")
db.commit()



#sql.execute(f"INSERT INTO cars VALUES (?, ?, ?)", (proba_name, proba_url, proba_price))
#db.commit()
