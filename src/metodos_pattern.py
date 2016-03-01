from pattern.web import *
from pattern.vector import *
from model.documento import *
from config import *
from enfoqueponderado import *
import os.path
import sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
#import para descargar pdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO



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
    try:
        url = URL(url)
        if extension(url.page) == ".pdf":
            f = open(url.domain + extension(url.page), 'wb') # save as test.gif
            f.write(url.download())
            f.close()
            contenido = convert_pdf_to_txt(url.domain+'.pdf')
            os.remove(url.domain + extension(url.page))
        else:
            contenido = plaintext(url.download(user_agent='Mozilla/5.0'))
    except Exception, e:
        print "Url: " + str(documento.url) + " - No se pudo descargar"
        print str(e)
        pass


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

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str
