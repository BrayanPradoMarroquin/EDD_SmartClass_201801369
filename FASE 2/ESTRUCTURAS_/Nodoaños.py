from ESTRUCTURAS_.ListaSemestre import ListSemestre

class Años:
    def __init__(self, anio):
        self.anio = anio
        self.mese = None
        self.semestre = ListSemestre()
        self.atras = None
        self.siguiente = None