from ESTRUCTURAS_.ARBOLB_.BTree import BTree

class Semestre:
    def __init__(self, semestre):
        self.semestre = semestre
        self.cursos = BTree()
        self.anterior = None
        self.siguiente = None
        