from pprint import pprint
import requests
from bs4 import BeautifulSoup as b
URL = 'https://www.ts.kg/category/cartoon_tv_series'
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req

html = get_html(URL)


def get_data(html):
    soup = b(html, 'html.parser')
    a = soup.find_all('div', class_='show')
    series = []
    for i in a:

        serial = {
            'title': i.find('a').find('p').getText,
            'link': i.find('a').get('href'),
        }
        series.append(serial)

    return series


pprint(get_data(html.text))
