class NodoCurso:
    def __init__(self, codigo, nombre, creditos, requisitos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.requisitos = requisitos.split(",")
        self.obligatorio = obligatorio
        self.siguiente = None
        self.anterior = None