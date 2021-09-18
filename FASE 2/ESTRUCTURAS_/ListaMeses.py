from ESTRUCTURAS_.NodoMeses import NodoMes
from ESTRUCTURAS_.Matriz import *

class Meses:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, mes):
        nuevo = NodoMes(mes)
        if self.inicio == None:
            self.inicio = nuevo
            self.final  = self.inicio
        else:
            cont = self.buscarmes(mes)
            if cont==False:
                self.final.siguiente = nuevo
                nuevo.atras = self.final
                ultimo = nuevo
    
    def buscarmes(self, mes):
        actual = self.inicio
        cond = False
        while (actual!=None) & (cond==False):
            if (actual.mes!=mes):
                actual = actual.siguiente
            else:
                cond = True
        
        if (actual==None):
            return False
        elif (actual.mes==mes):
            return True

    def añadircabeceras(self, mes, dia, hora, node):
        cond = False
        while(node!=None) & (cond==False):
            if(node.mes!=mes):
                node = node.siguiente
            else:
                node.matriz.filas.insertar(dia)
                node.matriz.columna.insertar(hora)
                cond=True
    
    def añadirtask(self, base, node):
        cond = False
        while(node!=None) & (cond==False):
            if(node.mes!=base.direccionamiento[1]):
                node = node.siguiente
            else:
                task = NodoData(+1, base.hora, base.direccionamiento[0])
                task.tareas.insertar(base)
                node.matriz.data.insertar(base.hora, base.direccionamiento[0], base.data.filas, base.data.columna, task)
                cond=True