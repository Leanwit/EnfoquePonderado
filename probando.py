# Import locales
from src.metodos_pattern import *
from pattern.vector import *
from src.config import *
from model.documento import *
from src.enfoqueponderado import *


# Import externos
import json
import os #Para recorrer dentro de una carpeta

archivo_json = open('json/urlclasificadas.txt','r')
json = json.load(archivo_json)

consulta = Document("tea quality in uk", stemmer = PORTER)

lista_documentos = []
for una_url in json['urls']:
    descargar_url(una_url['url'])
    doc = Documento()
    doc.url = una_url['url']
    doc.contenido = descargar_url_contenido(una_url['url'])
    doc.pattern = Document(doc.contenido,stemmer = PORTER)
    calcular_score_pattern(doc,consulta)
    lista_documentos.append(doc)

lista_documentos.sort(key=lambda x: x.score, reverse=True)

for doc in lista_documentos:
    print doc



# for file in os.listdir(path("Descargas/")):
#     if file.endswith(".txt"):
#         f = open(path("Descargas/"+file),"r")
#
#         documento = Document(f.read(), stemmer = PORTER)
#         lista_documentos.append(documento)
#
# model = Model(lista_documentos,  weight=TFIDF)
#
# for doc in model:
#     # for aux in doc.keywords(top=100):
#     calcular_score_pattern(doc,consulta)
