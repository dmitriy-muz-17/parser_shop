import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0', 'accept': '*/*'}
URL = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&country.import.usa.not=-1&price.currency=1&gearbox.id[1]=2&fuel.id[5]=6&abroad.not=0&custom.not=-1&page=0&size=12'

def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    elements = soup.find_all('div', class_='content-bar')
    e_cars = []
    for element in elements:
        e_cars.append({
            'name': element.find('span', class_='blue bold').get_text(strip=True),
            'link': element.find('a', class_='address').get('href'),
            'price_usd': element.find('span', class_='bold green size22').get_text(strip=True),
            'price_uah': element.find('span', class_='i-block').get_text(strip=True)
        })
    return  e_cars

def parse():
    html = get_html(URL)
    #print(html.status_code)
    if(html.status_code == 200):
        return get_content(html)
    else:
        print("Error with conection to web-site")
