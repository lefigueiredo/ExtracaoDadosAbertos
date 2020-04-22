from pyunpack import Archive
import pathlib

path = pathlib.Path('C:\\Users\\Letícia\\Documents\\Desafios Python do Carlo\\teste_download')
extensoes = (".zip",".tar",".rar",".7z")

for i in extensoes:
    for file in path.glob('**/*'+i):
        Archive(file).extractall(path)

