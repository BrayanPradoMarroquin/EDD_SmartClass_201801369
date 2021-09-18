from NodoTask import Tareas

class ListTareas:
    def __init__(self):
        self.inicio = None
    
    def insertar(self, nodo):
        if (self.inicio==None):
            self.inicio = nodo
        else:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo