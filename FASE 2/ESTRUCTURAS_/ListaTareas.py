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

    def actualizarTarea(self, id, carnet, nombre, descripcion, materia, fecha, hora, status):
        actual = self.inicio
        while(actual!=None):
            if(actual.id == id):
                actual.carnet = carnet
                actual.nombre = nombre
                actual.descripcion = descripcion
                actual.materia = materia
                actual.fecha = fecha
                actual.hora = hora
                actual.status = status
                break
            else: 
                actual = actual.siguiente

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

    def graficar(self):
        nodo = self.inicio
        data = open("ListTareas.dot", 'w', encoding='utf-8')
        data.write('digraph G { \n')
        data.write("rankdir=TB; \n")
        data.write("node [shape = circle, color=black , style=filled, fillcolor=gray93];\n")
        cont=0
        while(nodo!=None):
            data.write("Node"+ str(cont) + "[label=\" Carnet: " + str(nodo.carnet) + "\\n Tarea: " + nodo.nombre + "\\n Descripcion: " + nodo.descripcion + "\\n Materia: "+ nodo.materia +"\\n Fecha: "+nodo.fecha+ "\\n Hora: "+ nodo.hora +"\\n Estado: "+nodo.status+"\"];\n")
            if(nodo.siguiente!=None):
                data.write('Node'+str(cont-1)+"->Node"+str(cont))
            cont+=1
            nodo = nodo.siguiente
        data.write("} \n")
        data.close()
        os.system("dot -Tpng ListTareas.dot -o ListTareas.png")
        os.startfile("ListTareas.png")

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