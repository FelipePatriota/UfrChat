import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.ufrpe.br/br/lista-de-noticias"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \ (KHTML, like Gecko) Chrome / 86.6.4240.198Safari / 537.36"}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

quero = {'link': [], 'data': [], 'titulo': [], 'texto': []}

# pegando o número de páginas
for i in range(0,10):
    url_pag = f'http://www.uabj.ufrpe.br/br/noticias?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link = soup.find_all('div', class_=re.compile('views-field views-field-title'))
   
    for l in link:
        titulo = l.find('a').get_text().strip()
        if 'bolsas' in titulo:
            quero['titulo'].append(titulo)
            links = l.find('a').get('href')
            quero['link'].append(links)    
        d = soup.find_all('div', class_=re.compile('views-field-created'))
   
        for dado in d:
            data = dado.find('span', class_=re.compile('postado'))
            if data:
                data = data.get_text().strip()
                quero['data'].append(data)
            else:
                quero['data'].append("")

            t = soup.find_all('div', class_=re.compile('views-field views-field-title'))
   
            for titulo in t:
                titulo = titulo.find('a').get_text().strip()
                c = soup.find_all('div', class_=re.compile('views-field views-field-body'))
                for div in c:
                    soup = div.find('div', class_=re.compile('field field-name-body field-type-text-with-summary field-label-hidden'))
                    if soup is not None:
                        texto = soup.find_all('p')
                        texto = [t.get_text().strip() for t in texto]
                        texto = ' '.join(texto)
                        quero['texto'].append(texto)
                    else:
                        quero['texto'].append(None)

df = pd.DataFrame(quero)
df.to_csv('dados_uf.csv', index=False)
