from ESTRUCTURAS_.NodoCurso import NodoCurso

class Cursos:
    def __init__(self):
        self.inicio = None
        self.final = None
    
    def agregar(self, codigo, nombre, creditos, requisitos, obligatorio):
        Nuevo = NodoCurso(codigo, nombre, creditos, requisitos, obligatorio)
        if (self.inicio==None):
            self.inicio = Nuevo
            self.final = Nuevo
        else:
            self.final.siguiente = Nuevo
            Nuevo.anterior = self.final
            self.final = Nuevo