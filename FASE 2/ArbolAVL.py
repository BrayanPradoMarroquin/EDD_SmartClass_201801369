import NodoArbolAVL
import os

class ArbolAVL_:
    def __init__(self):
        self.root = None

    def max(self, v1, v2):
        if v1>v2:
            return v1
        else:
            return v2

    def tamaño(self, node):
        if node is not None:
            return node.height
        return -1

    def insert(self, value):
        self.root = self.insert_interno(value, self.root)

    def insert_interno(self, value, root):
        if root is None:
            return value
        else:
            if value.Carnet< root.Carnet:
                root.left = self.insert_interno(value, root.left)
                if self.tamaño(root.right) - self.tamaño(root.left) == -2:
                    if value.Carnet < root.left.Carnet:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif value.Carnet > root.Carnet:
                root.right = self.insert_interno(value, root.right)
                if self.tamaño(root.right) - self.tamaño(root.left) == 2:
                    if value.Carnet > root.right.Carnet:
                        root = self.RD(root)
                    else:
                        root = self.RDD(root)
            else:
                root.label = value
        
        root.height = self.max(self.tamaño(root.left), self.tamaño(root.right)) + 1
        return root

    def RI(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        node.height = self.max(self.tamaño(node.left), self.tamaño(node.right)) + 1
        aux.height = self.max(self.tamaño(aux.left), self.tamaño(aux.right)) + 1
        return aux

    def RD(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        node.height = self.max(self.tamaño(node.left), self.tamaño(node.right)) + 1
        aux.height = self.max(self.tamaño(aux.left), self.tamaño(aux.right)) + 1
        return aux

    def RDI(self, node):
        node.left = self.RD(node.left)
        return self.RI(node)

    def RDD(self, node):
        node.right = self.RI(node.right)
        return self.RD(node)

    def preShow(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.left)
            print(curr_node.Carnet, end=" ")
            self.preShow(curr_node.right)

    def Buscar_evento(self, node, Identificacion):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==Identificacion):
            return "El dato es: " + node.Carnet
        elif(Identificacion<node.Carnet):
            return self.Buscar_evento(node.left, Identificacion)
        elif(Identificacion>node.Carnet):
            return self.Buscar_evento(node.right, Identificacion)
    
    def graficar(self, node):
        file = open("ArbolAVL.dot", 'w')
        file.write("digraph G { \n")
        file.write("rankdir=TB; \n")
        file.write("node [shape = circle, color=black , style=filled, fillcolor=gray93];\n")        
        file.write(self.graficadora(node))
        file.write("} \n")
        file.close()
        os.system("dot -Tpng ArbolAVL.dot -o ArbolAVL_Alumnos.png")
        os.startfile("ArbolAVL_Alumnos.png")

    def graficadora(self, node):
        cadena=""
        if((node.left==None) & (node.right==None)):
            cadena = "nodo"+str(node.Carnet)+"[ label=\""+"\\n"+node.Carnet+"\\n"+node.Identificacion+"\\n "+node.Nombre+"\\n"+node.Carrera+"\\n"+"\\n"+node.Correo+"\\n"+node.Password+"\\n"+node.Creditos+"\\n"+node.Edad+"\"]; \n"
        else:
            cadena="nodo"+str(node.Carnet)+" [ label =\"<C0>|"+"\\n"+node.Carnet+"\\n"+node.Identificacion+"\\n "+node.Nombre+"\\n"+node.Carrera+"\\n"+"\\n"+node.Correo+"\\n"+node.Password+"\\n"+node.Creditos+"\\n"+node.Edad+"|<C1>\"];\n"
        
        if(node.left!=None):
            cadena = cadena + self.graficadora(node.left)+"nodo"+str(node.Carnet)+":C0->nodo"+str(node.left.Carnet)+"\n"
        if(node.right!=None):
            cadena = cadena + self.graficadora(node.right)+"nodo"+str(node.Carnet)+":C1->nodo"+str(node.right.Carnet)+"\n"
        
        return cadena