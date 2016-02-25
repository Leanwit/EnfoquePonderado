# Import locales
from metodos_pattern import *
from enfoqueponderado import *
from config import *
# Import externos
import json
import os #Para recorrer dentro de una carpeta

archivo_json = open('json/urlclasificadas.txt','r')
json = json.load(archivo_json)
for una_url in json['urls']:
    descargar_url(una_url['url'])

cadena = eliminar_stop_words("They are a house black and a LOLA sick")
print ' '.join(cadena)



for file in os.listdir(path("Descargas/")):
    if file.endswith(".txt"):
        f = open(path("Descargas/"+file),"r")
