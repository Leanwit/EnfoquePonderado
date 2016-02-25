from pattern.web import *
import os.path
import sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from config import *




def descargar_url(url):
    reload(sys)
    sys.setdefaultencoding('utf8')

    url = URL(url)
    directorio = "Descargas/"+str(url.domain)+".txt"
    if rewrite:
        f = open('Descargas/'+str(url.domain)+".txt",'wb')
        f.write(plaintext(url.download()))
        f.close
