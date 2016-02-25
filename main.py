# Import locales
from src.metodos_pattern import *
from src.enfoqueponderado import *
from src.config import *
from model.documento import *

# Import externos
import json
import os #Para recorrer dentro de una carpeta

archivo_json = open('json/urlclasificadas.txt','r')
json = json.load(archivo_json)
for una_url in json['urls']:
    descargar_url(una_url['url'])

# Primer paso, se elina las palabras vacias y se aplica stemming a la consulta
consulta = "Tea market, in india"
consulta = palabrasvacias_stemming(consulta)
print consulta

for file in os.listdir(path("Descargas/")):
    if file.endswith(".txt"):
        f = open(path("Descargas/"+file),"r")
        text = f.read()
        un_documento = Documento()
        un_documento.contenido = palabrasvacias_stemming(text)
        calcular_score(un_documento,consulta)
        un_documento.calcular_score()
        print un_documento
