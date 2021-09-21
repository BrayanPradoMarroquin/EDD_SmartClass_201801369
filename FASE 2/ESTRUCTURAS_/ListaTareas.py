from NodoTask import Tareas
import os

class ListTareas:
    def __init__(self):
        self.inicio = None
    
    def insertar(self, nodo):
        if (self.inicio==None):
            self.inicio = nodo
        else:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo

    

    def graficar(self):
        nodo = self.inicio
        data = open("ListTareas.dot", 'w', encoding='utf-8')
        data.write('digraph G { \n')
        data.write("rankdir=TB; \n")
        data.write("node [shape = circle, color=black , style=filled, fillcolor=gray93];\n")
        cont=0
        while(nodo!=None):
            data.write("Node"+ str(cont) + "[label=\" Carnet: " + str(nodo.carnet) + "\\n Tarea: " + nodo.nombre + "\\n Descripcion: " + nodo.descripcion + "\\n Materia: "+ nodo.materia +"\\n Fecha: "+nodo.fecha+ "\\n Hora: "+ nodo.hora +"\\n Estado: "+nodo.status+"\"];\n")
            if(nodo.atras!=None):
                data.write('Node'+str(cont-1)+"->Node"+str(cont))
            cont+=1
            nodo = nodo.siguiente
        data.write("} \n")
        data.close()
        os.system("dot -Tpng ListTareas.dot -o ListTareas.png")
        os.startfile("ListTareas.png")