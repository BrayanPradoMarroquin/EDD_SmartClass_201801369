import   ESTRUCTURAS_.NodoArbolAVL
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
                value.padre = root
                root.left = self.insert_interno(value, root.left)
                if self.tamaño(root.right) - self.tamaño(root.left) == -2:
                    if value.Carnet < root.left.Carnet:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif value.Carnet > root.Carnet:
                value.padre = root
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
            data = {
                'Carnet': node.Carnet,
                'DPI': node.Identificacion,
                'Nombre': node.Nombre,
                'Carrera': node.Carrera,
                'Correo': node.Correo,
                'Password': node.Password,
                'Creditos': node.Creditos,
                'Edad': node.Edad
            }

            return data
        elif(Identificacion<node.Carnet):
            return self.Buscar_evento(node.left, Identificacion)
        elif(Identificacion>node.Carnet):
            return self.Buscar_evento(node.right, Identificacion)

    def Mod_Estudiante(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad ,node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.Carnet = carnet
            node.Identificacion = DPI
            node.Nombre = nombre
            node.Carrera = carrera
            node.Correo = correo
            node.Password = password
            node.Creditos = creditos
            node.Edad = edad
        elif(carnet<node.Carnet):
            return self.Mod_Estudiante(carnet, DPI, nombre, carrera, correo, password, creditos, edad ,node.left)
        elif(carnet>node.Carnet):
            return self.Mod_Estudiante(carnet, DPI, nombre, carrera, correo, password, creditos, edad ,node.right)

    def AñadirAño(self, carnet, anio, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.años.insertar(anio)
            return "El dato es: " + node.Carnet
        elif(carnet<node.Carnet):
            return self.AñadirAño(carnet, anio, node.left)
        elif(carnet>node.Carnet):
            return self.AñadirAño(carnet, anio, node.right)

    def buscarmes(self, carnet, anio, mes, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.años.añadirmes(anio, mes, node.años.inicio)
        elif(carnet<node.Carnet):
            return self.buscarmes(carnet, anio, mes, node.left)
        elif(carnet>node.Carnet):
            return self.buscarmes(carnet, anio, mes, node.right)

    def buscarmatriz(self, carnet, anio, mes, dia, hora, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.años.buscarmes(anio, mes, dia, hora, node.años.inicio)
        elif(carnet<node.Carnet):
            return self.buscarmatriz(carnet, anio, mes, dia, hora, node.left)
        elif(carnet>node.Carnet):
            return self.buscarmatriz(carnet, anio, mes, dia, hora, node.right)

    def litareas(self, base, node, accion):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==base.carnet):
            node.años.tasklist(base, node.años.inicio, accion)
        elif(base.carnet<node.Carnet):
            return self.litareas(base, node.left, accion)
        elif(base.carnet>node.Carnet):
            return self.litareas(base, node.right, accion)

    def newAll(self, Tarea, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==Tarea.carnet):
            self.AñadirAño(Tarea.carnet, Tarea.direccionamiento[2], node)
            self.buscarmes(Tarea.carnet, Tarea.direccionamiento[2], Tarea.direccionamiento[1], node)
            self.buscarmatriz(Tarea.carnet, Tarea.direccionamiento[2], Tarea.direccionamiento[1], Tarea.direccionamiento[0], Tarea.hora, node)
            self.litareas(Tarea, node, "añadir")
            self.litareas(Tarea, node, "tarea")
        elif(Tarea.carnet<node.Carnet):
            return self.newAll(Tarea, node.left)
        elif(Tarea.carnet>node.Carnet):
            return self.newAll(Tarea, node.right)

    def RecuTarea(self, carnet, anio, mes, dia, hora, id, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            return node.años.RecuTarea(anio, mes, dia, hora, id)
        elif(carnet<node.Carnet):
            return self.RecuTarea(carnet, anio, mes, dia, hora, id, node.left)
        elif(carnet>node.Carnet):
            return self.RecuTarea(carnet, anio, mes, dia, hora, id, node.right)

    def actualizarTarea(self, carnet, anio, mes, dia, hora, id, nombre, descripcion, materia, fecha, status, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            return node.años.actualizarTarea(anio, mes, dia, hora, id, carnet, nombre, descripcion, materia, fecha, status)
        elif(carnet<node.Carnet):
            return self.actualizarTarea(carnet, anio, mes, dia, hora, id, node.left)
        elif(carnet>node.Carnet):
            return self.actualizarTarea(carnet, anio, mes, dia, hora, id, node.right)    

    def buscarsemestre(self, carnet, anio, semestre, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.años.añadirsemestre(anio, semestre, node.años.inicio)
        elif(carnet<node.Carnet):
            return self.buscarsemestre(carnet, anio, semestre, node.left)
        elif(carnet>node.Carnet):
            return self.buscarsemestre(carnet, anio, semestre, node.right)

    def cursosEstudiante(self, carnet, anio, semestre, codigo, curso, creditos, pre, ob, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.años.añadirCurso(anio, semestre, codigo, curso, creditos, pre, ob, node.años.inicio)
        elif(carnet<node.Carnet):
            return self.cursosEstudiante(carnet, anio, semestre, codigo, curso, creditos, pre, ob, node.left)
        elif(carnet>node.Carnet):
            return self.cursosEstudiante(carnet, anio, semestre, codigo, curso, creditos, pre, ob, node.right)

    def graphTareas(self, carnet, año, mes, dia, hora, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Carnet==carnet):
            node.años.graficarTarea(año, mes, dia, hora, node.años.inicio)
        elif(carnet<node.Carnet):
            return self.graphTareas(carnet, año, mes, dia, hora, node.left)
        elif(carnet>node.Carnet):
            return self.graphTareas(carnet, año, mes, dia, hora, node.right)

    def graficar(self, node):
        file = open("ArbolAVL.dot", 'w')
        file.write("digraph G { \n")
        file.write("rankdir=TB; \n")
        file.write("node [shape = record, color=black , style=filled, fillcolor=gray93];\n")        
        file.write(self.graficadora(node))
        file.write("} \n")
        file.close()
        os.system("dot -Tpng ArbolAVL.dot -o ArbolAVL_Alumnos.png")
        os.startfile("ArbolAVL_Alumnos.png")

    def graficadora(self, node):
        cadena=""
        if((node.left==None) & (node.right==None)):
            cadena = "nodo"+str(node.Carnet)+"[ label=\""+"\\n Carnet: "+node.Carnet+"\\n DPI: "+node.Identificacion+"\\n Nombre: "+node.Nombre+"\\n Carrera: "+node.Carrera+"\\n Correo: "+node.Correo+"\\n Password: "+node.Password+"\\n Creditos: "+node.Creditos+"\\n Edad: "+node.Edad+"\"]; \n"
        else:
            cadena="nodo"+str(node.Carnet)+" [ label =\"<C0>| Carnet: "+node.Carnet+"\\n DPI: "+node.Identificacion+"\\n Nombre: "+node.Nombre+"\\n Carrera: "+node.Carrera+"\\n Correo: "+node.Correo+"\\n Password: "+node.Password+"\\n Creditos: "+node.Creditos+"\\n Edad: "+node.Edad+"|<C1>\"];\n"
        
        if(node.left!=None):
            cadena = cadena + self.graficadora(node.left)+"nodo"+str(node.Carnet)+":C0->nodo"+str(node.left.Carnet)+"\n"
        if(node.right!=None):
            cadena = cadena + self.graficadora(node.right)+"nodo"+str(node.Carnet)+":C1->nodo"+str(node.right.Carnet)+"\n"
        
        return cadena