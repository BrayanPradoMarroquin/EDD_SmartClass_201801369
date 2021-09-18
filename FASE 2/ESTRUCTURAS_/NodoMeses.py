from ESTRUCTURAS_.nodoBaseM import NodoMatriz

class NodoMes:
    def __init__(self, mes):
        self.mes = mes
        self.anterior = None
        self.siguiente = None
        self.matriz = NodoMatriz()