from pattern.web import *
from pattern.vector import *
from model.documento import *
from config import *
from enfoqueponderado import *
import os.path
import sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
# import string


def descargar_url(url):
    reload(sys)
    sys.setdefaultencoding('utf8')
    url = URL(url)
    directorio = "Descargas/"+str(url.domain)+".txt"
    if rewrite:
        f = open('Descargas/'+str(url.domain)+".txt",'wb')
        contenido = plaintext(url.download())
        f.write(contenido)
        f.close

def descargar_url_contenido(url):
    reload(sys)
    sys.setdefaultencoding('utf8')
    url = URL(url)
    contenido = plaintext(url.download())
    return contenido

# No se utiliza debido al stemming de pattern
def quitar_simbolos(cadena):
    simbolos = (open("Herramientas/diccionario_simbolos.txt","r").read()).split()
    for simbolo in simbolos:
        cadena = cadena.replace(simbolo,"")
    return cadena
# No se utiliza debido al stemming de pattern
def eliminar_stop_words(cadena):
    cadena = cadena.split()
    diccionario = (open("Herramientas/diccionario_stop_words_en.txt","r").read()).split()
    for palabra in diccionario:
        for indice, termino in enumerate(cadena):
            if termino == palabra:
                del cadena[indice]
    return cadena
# No se utiliza debido al stemming de pattern
def stemming(cadena):
    cadena = [stem(word) for sentence in cadena for word in sentence.split(" ")]
    return cadena
# No se utiliza debido al stemming de pattern
def palabrasvacias_stemming(cadena):
    # quita simbolos especiales
    cadena = quitar_simbolos(cadena)
    cadena = eliminar_stop_words(cadena)
    cadena = stemming(cadena)
    return cadena
