from NodoTask import Tareas
import os

class ListTareas:
    def __init__(self):
        self.inicio = None
    
    def insertar(self, nodo):
        if (self.inicio==None):
            self.inicio = nodo
        else:
            nodo.siguiente = self.inicio
            self.inicio = nodo

    def buscartarea(self, id):
        actual = self.inicio
        while(actual!=None):
            if(str(actual.id) == id):
                data = {
                    'Carnet':actual.carnet,
                    'nombre':actual.nombre,
                    'descripcion': actual.descripcion,
                    'materia': actual.materia,
                    'fecha': actual.fecha,
                    'hora': actual.hora,
                    'Estado': actual.status
                }
                return data
            else:
                actual = actual.siguiente


    def Eliminar(self, id):
        actual = self.inicio
        previo = None
        val = True 

        while(actual!=None & val==False):
            if(actual.id==id):
                if(previo==None):
                    previo=actual.siguiente
                    actual.sigueinte=None
                else:
                    previo.siguiente = actual.siguiente
                    actual.siguiente = None
                val=True
            else:
                previo=actual
                actual=actual.siguiente