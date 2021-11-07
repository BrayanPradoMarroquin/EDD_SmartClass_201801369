import os
class Arista():
    def __init__(self, codigo, curso, creditos, pre):
        self.codigo = codigo
        self.curso = curso
        self.creditos = creditos 
        self.pre = pre
        self.siguiente = None

class Grafo():
    def __init__(self):
        self.inicio = None

    def agregar(self, Arista):
        if (self.inicio==None):
            self.inicio = Arista
        else:
            if (self.validar(Arista.codigo)==False):
                Arista.siguiente = self.inicio
                self.inicio = Arista

    def validar(self, codigo):
        actual = self.inicio
        while(actual!=None):
            if(codigo==actual.codigo):
                return True
            else:
                actual = actual.siguiente
        return False

    def graficar(self):
        actual = self.inicio
        cadena = ""
        file = open("FRONTEND/front/src/assets/Grafo.dot", 'w', encoding="utf-8")
        file.write("digraph G { \n")
        file.write("charset=\"UTF-8\" \n" )
        file.write("rankdir=TB; \n")
        file.write("node [shape = rectangle, color=black , style=filled, fillcolor=gray93];\n")
        while(actual!=None):
            cadena += "nodo"+actual.codigo+"[label=\""+actual.codigo+"\\n "+actual.curso+"\" ]; \n"
            for pre in actual.pre:
                if(pre!=""):
                    cadena += "nodo"+pre+" -> nodo"+actual.codigo+"[label=\""+str(actual.creditos)+"\"]\n"
            actual = actual.siguiente
        file.write(cadena)
        file.write("} \n")
        file.close()
        os.system("dot -Tpng FRONTEND/front/src/assets/Grafo.dot -o FRONTEND/front/src/assets/Grafo.png")
        os.system("dot -Tpng FRONTEND/front/src/assets/Grafo.dot -o FRONTEND/front/src/assets/Grafo2.png")