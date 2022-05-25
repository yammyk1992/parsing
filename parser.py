import json
from dataclasses import asdict, dataclass

import requests
from bs4 import BeautifulSoup
from pprint import pprint


@dataclass
class Parse:
    title: str
    subtitles: list


url = 'https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-online'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)',
           'accept': '*/*'
           }


def get_html(url, headers):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all("div", class_="t517__sectioninfowrapper")

    themes = []

    for item in items:
        title = item.find("strong")
        text = item.find_all("li")

        subtitles = []

        for t in text:
            subtitles.append(t.text.strip())

        themes.append(asdict(Parse(title.text.strip(), subtitles)))
        # 'title': item.find('div', class_='t-name t-name_lg t517__bottommargin'),
        # 'subtitles': item.find('div', class_="t-text t-text_sm")
        # })
    return json.dumps(themes, indent=4, ensure_ascii=False)


print(get_html(url, headers))
#
#
# def parse():
#     html = get_html(URL)
#     if html.status_code == 200:
#         get_content(html.text)
#     else:
#         print('error')
#
#
# parse()
