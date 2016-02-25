def eliminacion_palabras_parada():
    return "Nada por ahora"

def stemming():
    return "Nada por ahora"

def tokenization():
    return "Nada por ahora"

def construir_diccionario_dominio():
    return "Nada por ahora"

def eliminar_stop_words(cadena):
    cadena = cadena.split()
    diccionario = (open("Herramientas/diccionario_stop_words_en.txt","r").read()).split()
    for palabra in diccionario:
        for indice, termino in enumerate(cadena):
            if termino == palabra:
                del cadena[indice]
    return cadena
