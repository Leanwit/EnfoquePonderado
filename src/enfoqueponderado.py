from pattern.web import *
from pattern.vector import *
from model.documento import *
from src.metodos_pattern import *
import json
import os #Para recorrer dentro de una carpeta
lista_documentos = []

def calcular_score_pattern(documento,consulta):
    acierto_clave = 0
    acierto_positivo = 0
    acierto_negativo = 0

    diccionario_dominio = (open("Herramientas/diccionario_dominio.txt","r").read()).split()
    diccionario_dominio = Document(diccionario_dominio, stemmer = PORTER)
    # print consulta.words
    for doc in documento.pattern.keywords(top=200,normalized=True):

        if doc[1] in consulta:
            acierto_clave += doc[0]
            print "Entro AC -> " + str(doc[1]) + " - " + str(doc[0])
        else:
            if doc[1] in diccionario_dominio.words:
                # print "Entro AP -> " + str(doc[1]) + " - " + str(doc[0])
                acierto_positivo += doc[0]
            else:
                # print "Entro AN -> " + str(doc[1]) + " - " + str(doc[0])
                acierto_negativo += doc[0]


    documento.acierto_clave = acierto_clave
    documento.acierto_positivo = acierto_positivo
    documento.acierto_negativo = acierto_negativo
    documento.calcular_score()


def opcion_json(consulta,var_json):

    for una_url in var_json['urls']:
        descargar_url(una_url['url'])
        doc = Documento()
        doc.url = una_url['url']
        doc.contenido = descargar_url_contenido(una_url['url'])
        doc.pattern = Document(doc.contenido,stemmer = PORTER)
        calcular_score_pattern(doc,consulta)
        lista_documentos.append(doc)
    return lista_documentos

def opcion_prueba(consulta):
    doc = Documento()
    doc.url = "teamarketonline.com"
    doc.contenido = open('Descargas/teamarketonline.com.txt','r').read()
    doc.pattern = Document(doc.contenido,stemmer = PORTER)
    calcular_score_pattern(doc,consulta)
    lista_documentos.append(doc)

    doc = Documento()
    doc.url = "www.euromonitor.com"
    doc.contenido = open('Descargas/www.euromonitor.com.txt','r').read()
    doc.pattern = Document(doc.contenido,stemmer = PORTER)
    calcular_score_pattern(doc,consulta)
    lista_documentos.append(doc)

    doc = Documento()
    doc.url = "www.teavivre.com"
    doc.contenido = open('Descargas/www.teavivre.com.txt','r').read()
    doc.pattern = Document(doc.contenido,stemmer = PORTER)
    calcular_score_pattern(doc,consulta)
    lista_documentos.append(doc)
    return lista_documentos
