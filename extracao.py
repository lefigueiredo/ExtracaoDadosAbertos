import requests
import urllib.request
import time
from bs4 import BeautifulSoup

html = requests.get('http://portal.inep.gov.br/microdados')     #Site para vasculhar o codigo fonte
soup = BeautifulSoup(html.text, "html.parser")         # Puxa os dados do codigo fonte e deixa legivel

divs = soup.find_all('div', {"class": "list-download--two-columns-programs anchor__content"})       # Puxa a primeira leva de download de uma determinada categoria

for div in divs:
    nome = div.find_all('h4')[0].text

    links = div.find_all('a')#Iteraçao de todos os links na categoria
    if len(links) >= 3:     #Condiçao que ve a quantidade de itens na lista
        for i in range(-3,0):      #Passar por 3 itens da lista
            urllib.request.urlretrieve(links[i]['href'], f'{nome}{i}.zip')       # Baixa os links de indice -3, -2, -1 nessa ordem e adiciona o nome no final
            time.sleep(1)
    else:       #Caso tenha menos de 3 itens
        for i in range(0,len(links)):     #Passar por todos os links e baixar todos
            urllib.request.urlretrieve(links[i]['href'], f'{nome}{i}.zip')
            time.sleep(1)
