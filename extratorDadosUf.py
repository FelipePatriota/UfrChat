import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import math

url = "https://www.ufrpe.br/br/lista-de-noticias"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \ (KHTML, like Gecko) Chrome / 86.6.4240.198Safari / 537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

quero = {'link': [], 'data': []}

for i in range(0, 3):
    url_pag = f'https://www.ufrpe.br/br/lista-de-noticias?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link = soup.find_all('div', class_=re.compile('views-field views-field-title'))

    for l in link:
        links = l.find('a').get('href')
        quero['link'].append(links)

    d = soup.find_all('div', class_=re.compile('views-field-created'))
    for dado in d:
        data = dado.find('span', class_=re.compile('postado')).get_text().strip()
        quero['data'].append(data)



df = pd.DataFrame(quero)
df.to_csv('dados_uf.csv', index=False)
