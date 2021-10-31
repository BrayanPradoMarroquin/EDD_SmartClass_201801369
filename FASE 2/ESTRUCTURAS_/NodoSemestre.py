from ESTRUCTURAS_.ListaCursos import Cursos

class Semestre:
    def __init__(self, semestre):
        self.semestre = semestre
        self.cursos = Cursos()
        self.anterior = None
        self.siguiente = None
        