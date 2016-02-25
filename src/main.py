import json
from enfoqueponderado import *

archivo_json = open('json/urlclasificadas.txt','r')
json = json.load(archivo_json)


cadena = eliminar_stop_words("They are a house black and a LOLA sick")
print ' '.join(cadena)
