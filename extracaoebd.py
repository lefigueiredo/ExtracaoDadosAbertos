import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pyunpack import Archive
import pathlib


def unpack():
    path = pathlib.Path('C:\\Users\\Letícia\\Documents\\Desafios Python do Carlo')
    extensoes = (".zip", ".tar", ".rar", ".7z")

    for i in extensoes:
        for file in path.glob('**/*' + i):
            Archive(file).extractall(path)


def extracao():
    html = requests.get('http://portal.inep.gov.br/microdados')
    soup = BeautifulSoup(html.text, "html.parser")
    divs = soup.find_all('div', {"class": "list-download--two-columns-programs anchor__content"})

    for div in divs:
        nome = div.find_all('h4')[0].text
        links = div.find_all('a')

        if len(links) >= 3:
            for i in range(-3, 0):
                urllib.request.urlretrieve(links[i]['href'], f'{nome}{i}.zip')
                time.sleep(1)

        else:
            for i in range(0, len(links)):
                urllib.request.urlretrieve(links[i]['href'], f'{nome}{i}.zip')
                time.sleep(1)

        unpack()