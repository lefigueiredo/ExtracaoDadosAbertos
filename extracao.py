import requests     #Biblioteca que pega coisas na web
import urllib.request       #Bibliteca que baixa os itens da web
import time         #Bibliotea que gerencia tempo
from bs4 import BeautifulSoup           #Biblioteca que torna legivel o codigo fonte do site

''' Importante informar que o download é feito na pasta em que o arquivo .py se encontra'''

html = requests.get('http://portal.inep.gov.br/microdados')     #Site para vasculhar o codigo fonte
soup = BeautifulSoup(html.text, "html.parser")         # Puxa os dados do codigo fonte e deixa legivel

divs = soup.find_all('div', {"class": "list-download--two-columns-programs anchor__content"})       # Puxa a primeira leva de download de uma determinada categoria
''' Nesse caso em espcial, as categorias para download estao separadas por div no site e obrigatoriamente cada div
possui a mesma classe. Por esse motivo, se faz uma varredura somente pelas divs que contenham uma classe
especifica para fazer o download. '''

for div in divs:        #Itaracao de cada categoria, individualmente dentro das divs das categorias para download
    nome = div.find_all('h4')[0].text
    '''Pega o nome da categoria no codigo fonte (os nomes estão inseridos no <h4> e como só tem um, por isso [0]) '''

    links = div.find_all('a')       #Iteraçao de todos os links de download na categoria
    '''Faz uma lista com todos os links para fazer download dentro da div que está dentro da iteracao anterior
     (no caso todos os links de download estao dentro de um <a>)'''

    if len(links) >= 3:     #Condiçao que ve a quantidade de itens na lista
        for i in range(-3,0):      #Passar pelos 3 ultimos itens da lista porque só se quer os tres ultimos anos
            urllib.request.urlretrieve(links[i]['href'], f'{nome}{i}.zip')       # Baixa os links de indice -3, -2, -1 nessa ordem e adiciona o nome no final (2 parametros)
            '''urllib.request  -> pega o link da web
               urlretrieve(  -> faz o download do link da web
               links[i]['href']   -> links sao todos os links dentro da div \ [i] é a iteracao dos ultimos
                                     3 indices \ ['href'] é a referencia no codigo fonte que indica que o 
                                     que esta apos ele é o link para download
               f'{nome}{i}.zip'    -> (esta após a virgula por ser segundo parametro) é o nome que se vai dar
                                       para esse arquivo quando fizer o download. {nome} é o nome da categoria
                                       que pegamos dentro do <h4> da div \ {i} é a iteracao que se encontra o 
                                       arquivo (fica a criterio de cada situacao colocar esse nome). '''
            time.sleep(1)       # Esperar 1 segundo para proximo download, dessa forma o site não nos classifica como spammer

    else:       #Caso tenha menos de 3 itens para download
        for i in range(0,len(links)):     #Passar por todos os links e baixar todos
            urllib.request.urlretrieve(links[i]['href'], f'{nome}{i}.zip')
            time.sleep(1)       # Esperar 1 segundo para proximo download, dessa forma o site não nos classifica como spammer
