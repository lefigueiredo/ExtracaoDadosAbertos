from pyunpack import Archive
import pathlib
import os
###############################################
''' Fazendo a varredura dentro da pasta dos downloads tipo 01 '''

path = pathlib.Path('C:\\Users\\Letícia\\Documents\\Desafios Python do Carlo\\teste_download')

extensoes = (".zip",".tar",".rar",".7z")
for i in extensoes:
    for file in sorted(path.glob('**/*'+i)):
        Archive(file).extractall(path)

