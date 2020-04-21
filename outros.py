import pathlib
from pyunpack import Archive
import os
###############################################
''' Fazendo a varredura dentro da pasta dos downloads tipo 01 '''

# path = os.listdir('C:\\Users\\Letícia\\Documents\\Desafios Python do Carlo\\teste_download')
# extensoes = (".zip",".tar",".rar",".7z")
# for i in path:
#     if i.endswith(extensoes):
#         print('deu')
#     else:
#         print('fodeu')

###############################################
''' Fazendo a varredura dentro da pasta dos downloads tipo 02 '''

extensoes = (".zip",".tar",".rar",".7z")

diretorio = pathlib.Path('C:\\Users\\Letícia\\Documents\\Desafios Python do Carlo\\teste_download')
print(sorted(diretorio.glob('**/.rar')))










#################################################