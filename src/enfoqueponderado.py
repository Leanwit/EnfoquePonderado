from stemming.porter2 import stem #Stemming


import string


def eliminacion_palabras_parada():
    return "Nada por ahora"

def stemming():
    return "Nada por ahora"

def tokenization():
    return "Nada por ahora"

def construir_diccionario_dominio():
    return "Nada por ahora"


def quitar_simbolos(cadena):
    simbolos = (open("Herramientas/diccionario_simbolos.txt","r").read()).split()
    for simbolo in simbolos:
        cadena = cadena.replace(simbolo,"")
    return cadena

def eliminar_stop_words(cadena):
    cadena = cadena.split()
    diccionario = (open("Herramientas/diccionario_stop_words_en.txt","r").read()).split()
    for palabra in diccionario:
        for indice, termino in enumerate(cadena):
            if termino == palabra:
                del cadena[indice]
    return cadena

def stemming(cadena):
    cadena = [stem(word) for sentence in cadena for word in sentence.split(" ")]
    return cadena

def palabrasvacias_stemming(cadena):
    # quita simbolos especiales
    cadena = quitar_simbolos(cadena)
    cadena = eliminar_stop_words(cadena)
    cadena = stemming(cadena)
    return cadena

def calcular_score_pattern(documento,consulta):
    acierto_clave = 0
    acierto_positivo = 0
    acierto_negativo = 0

    diccionario_dominio = (open("Herramientas/diccionario_dominio.txt","r").read()).split()
    for doc in documento.pattern.keywords(top=100):
        for termino_consulta in consulta:
            if doc[1] == termino_consulta:
                acierto_clave += doc[0]
            else:
                for termino_diccionario in diccionario_dominio:
                    if doc[1] == termino_diccionario:
                        acierto_positivo += doc[0]
                    else:
                        acierto_negativo += doc[0]

    documento.acierto_clave = acierto_clave
    documento.acierto_positivo = acierto_positivo
    documento.acierto_negativo = acierto_negativo
    documento.calcular_score()
