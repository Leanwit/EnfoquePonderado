from pattern.vector import *
from src.config import *

consulta = Document("Tea quality")

for file in os.listdir(path("Descargas/")):
    if file.endswith(".txt"):
        f = open(path("Descargas/"+file),"r")
        documento = Document(f.read())
        print documento.tfidf(consulta)
