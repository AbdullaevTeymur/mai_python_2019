import requests
from bs4 import BeautifulSoup
import json
import re
url = 'https://www.dme.ru/shopping/shop/'
domain = "".join(re.findall('(https?://)?(www\.)?([-\w.]+)', url)[0])
stran = requests.get(url).text
c = BeautifulSoup(stran, 'lxml')
mag = {}

dan = (c.find('div', class_='shadows_left')
            .find('div', class_='shadows_right')
            .find('div', class_='layout')
            .find('div', class_='main')
            .find('div', class_='right_column')
            .find('div', class_='content')
            .find('div', class_='simple')
            .find('div', class_='simple')
            .find('div')
            .find('div'))


dan = dan.findAll(['a', 'h2', 'p'])

key = ''
for item in dan:
        if item.name == 'h2':
            mag.update({item.text: {'title': item.text, 'place': 'неизвестно', 'magazins': []}})
            key = item.text

        elif key and item.name == 'p' and 'располож' in item.text:
            pattern = re.compile('расположен[\w]?\s', re.IGNORECASE)
            mag[key]['place'] = re.split(pattern, item.text)[1]

        elif key and item.name == 'a' and item.text:
            mag_url = domain + (item.attrs["href"] if item.attrs['href'][0] == '/' else f'/{item.attrs["href"]}')
            mag[key]['magazins'].append({'title': item.text, 'url': mag_url})

with open('Zach.json', 'w', encoding='utf-8') as f:
     json.dump(mag, f, ensure_ascii=False)
