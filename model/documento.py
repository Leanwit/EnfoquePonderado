
class Documento():
    url = ""
    contenido = ""
    acierto_clave = 0
    acierto_positivo = 0
    acierto_negativo = 0
    score = 0
    pattern = ""


    def __repr__(self):
        return "Score: " + str(self.score) + " | " + "AC: "+ str(self.acierto_clave) + " | " + "AP:" + str(self.acierto_positivo) + " | " + "AN: " + str(self.acierto_negativo) + "Url: " + str(self.url)


    def calcular_score(self):
        self.score = ((self.acierto_clave)+(self.acierto_positivo * 0.75) + (self.acierto_negativo*0.5)) / (self.acierto_clave+self.acierto_positivo+self.acierto_negativo)
