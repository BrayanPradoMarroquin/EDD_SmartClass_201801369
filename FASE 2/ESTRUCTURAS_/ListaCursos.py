from ESTRUCTURAS_.NodoCurso import NodoCurso
import os

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

    def buscar(self, codigo):
        actual = self.inicio
        while(actual!=None):
            if(codigo==actual.codigo):
                return [actual.codigo, actual.nombre, actual.creditos, actual.requisitos]
            else:
                actual = actual.siguiente
        return ""

    def graficar(self):
        actual = self.inicio
        cadena = ""
        file = open("FRONTEND/front/src/assets/Pensum.dot", 'w', encoding="utf-8")
        file.write("digraph G { \n")
        file.write("charset=\"UTF-8\" \n" )
        file.write("rankdir=TB; \n")
        file.write("node [shape = rectangle, color=black , style=filled, fillcolor=gray93];\n")
        while(actual!=None):
            cadena += "nodo"+actual.codigo+"[label=\""+actual.codigo+"\\n "+actual.nombre+"\" ]; \n"
            for pre in actual.requisitos:
                if(pre!=""):
                    cadena += "nodo"+pre+" -> nodo"+actual.codigo+"\n"
            actual = actual.siguiente
        file.write(cadena)
        file.write("} \n")
        file.close()
        os.system("dot -Tpng FRONTEND/front/src/assets/Pensum.dot -o FRONTEND/front/src/assets/Pensum.png")