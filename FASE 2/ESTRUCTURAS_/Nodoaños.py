from ESTRUCTURAS_.ListaMeses import Meses

class Años:
    def __init__(self, anio):
        self.anio = anio
        self.mese = Meses()
        self.semestre = None
        self.atras = None
        self.siguiente = None