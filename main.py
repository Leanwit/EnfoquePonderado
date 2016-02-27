# Import locales
# from src.metodos_pattern import *
from pattern.vector import *
from src.config import *
from model.documento import *
from src.enfoqueponderado import *

# Import externos
import json
import os #Para recorrer dentro de una carpeta

archivo_json = open('json/urlclasificadas.txt','r')
var_json = json.load(archivo_json)
print "Proyecto => " + var_json['id_proyecto']

lista_documentos = []
consulta = Document("tea quality in UK", stemmer = PORTER)
opcion = raw_input("1. Json - 2. Prueba: ")
if opcion == "1":
    lista_documentos  = opcion_json(consulta,var_json)
else:
    if opcion == "2":
        lista_documentos = opcion_prueba(consulta)
    else:
        sys.exit(0)

lista_documentos.sort(key=lambda x: x.score, reverse=True)

# creando la respuesta de las url con su orden
respuesta = {}
respuesta['id_proyecto'] = var_json['id_proyecto']
respuesta['nombre_directorio'] = var_json['nombre_directorio']
respuesta['urls'] = []

for indice,doc in enumerate(lista_documentos):
    urls_json = {}
    urls_json['orden'] = indice+1
    urls_json['url'] = doc.url
    respuesta['urls'].append(urls_json)
    print doc
json_data = json.dumps(respuesta,sort_keys=True,indent=4)
f = open("json/url_respuestas.txt", "wb").write(json_data)
