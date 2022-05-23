import requests
import style as style
from bs4 import BeautifulSoup
import csv

HOST = 'https://teachmeskills.by/'
URL = 'https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-online'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)',
           'accept': '*/*'
           }


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='t517__sectioninfowrapper')

    themes = []

    for item in items:
        themes.append({
            'title': item.find('div', class_='t-name t-name_lg t517__bottommargin'),
            'subtitles': item.find('div', class_="t-text t-text_sm")
        })
    print(themes)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')


parse()
