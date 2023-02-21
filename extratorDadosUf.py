import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import math
# url de onde será extraído os dados
url = "https://www.ufrpe.br/br/lista-de-noticias"

# cabeçalho para simular um navegador
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \ (KHTML, like Gecko) Chrome / 86.6.4240.198Safari / 537.36"}

# fazendo a requisição
site = requests.get(url, headers=headers)

# transformando o conteúdo em um objeto BeautifulSoup
soup = BeautifulSoup(site.content, 'html.parser')

# criando um dicionário para armazenar os dados que serão extraídos
quero = {'link': [], 'data': [], 'titulo': [], 'texto': []}

# pegando o número de páginas
for i in range(0,3):
    url_pag = f'https://www.ufrpe.br/br/lista-de-noticias?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link = soup.find_all('div', class_=re.compile('views-field views-field-title'))
   
    # for para pegar os links
    for l in link:
        links = l.find('a').get('href')
        quero['link'].append(links)    
    d = soup.find_all('div', class_=re.compile('views-field-created'))
   
    # for para pegar a data
    for dado in d:
        data = dado.find('span', class_=re.compile('postado')).get_text().strip()
        quero['data'].append(data)
    t = soup.find_all('div', class_=re.compile('views-field views-field-title'))
   
    # for para pegar o título
    for titulo in t:
        titulo = titulo.find('a').get_text().strip()
        quero['titulo'].append(titulo)
    c = soup.find_all('div', class_=re.compile('views-field views-field-body'))


numero = len (quero['link'])
for i in range(numero):
    url_p = 'https://www.ufrpe.br/' + quero['link'][i]	
    site = requests.get(url_p, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    conteudo = soup.find('div', class_=re.compile('field field-name-body field-type-text-with-summary field-label-hidden'))
    texto = conteudo.find('p').get_text().strip()
    quero['texto'].append(texto)
    



df = pd.DataFrame(quero)
df.to_csv('dados_uf.csv', index=False)

