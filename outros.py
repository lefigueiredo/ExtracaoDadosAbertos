from pyunpack import Archive
import os
###############################################
''' Fazendo a varredura dentro da pasta dos downloads tipo 01 '''

path = ('C:\\Users\\Letícia\\Documents\\Desafios Python do Carlo\\teste_download\\')

extensoes = (".zip",".tar",".rar",".7z")
for i in os.listdir(path):
    if i.endswith(extensoes):
        Archive(path+i).extractall(path)
