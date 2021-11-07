import ESTRUCTURAS_.NodoArbolAVL
from cryptography.fernet import Fernet
import os
import hashlib

file = open('key.key', 'rb')
key = file.read()
file.close()
keygen = Fernet(key)

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
            if value.Val< root.Val:
                value.padre = root
                root.left = self.insert_interno(value, root.left)
                if self.tamaño(root.right) - self.tamaño(root.left) == -2:
                    if value.Val < root.left.Val:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif value.Val > root.Val:
                value.padre = root
                root.right = self.insert_interno(value, root.right)
                if self.tamaño(root.right) - self.tamaño(root.left) == 2:
                    if value.Val > root.right.Val:
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
            print(curr_node.Val, end=" ")
            self.preShow(curr_node.right)

    def Buscar_evento(self, node, Identificacion, contrasenia):
        if(Identificacion=="admin") & (contrasenia=="admin"):
            data = {
                'status': "admin"
            }
            return data
        elif(Identificacion=="admin") & (contrasenia!="admin"):
            data = {
                'status': "Pas"
            }
            return data
        elif(node==None):
            data = {
                'status': "No"
            }
            return data
        elif(node.Val==Identificacion) & (keygen.decrypt(node.Password).decode()!=hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()):
            data = {
                'status': "Pas"
            }
            return data
        elif(node.Val==Identificacion) & (keygen.decrypt(node.Password).decode()==hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()):
            data = {
                'status': "Yes",
                'nombre': keygen.decrypt(node.Nombre).decode(),
                'carnet': Identificacion
            }
            return data
        elif(Identificacion<node.Val):
            return self.Buscar_evento(node.left, Identificacion, contrasenia)
        elif(Identificacion>node.Val):
            return self.Buscar_evento(node.right, Identificacion, contrasenia)

    def Mod_Estudiante(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad ,node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.Identificacion = DPI
            node.Nombre = nombre
            node.Carrera = carrera
            node.Correo = correo
            node.Password = password
            node.Creditos = creditos
            node.Edad = edad
        elif(carnet<node.Val):
            return self.Mod_Estudiante(carnet, DPI, nombre, carrera, correo, password, creditos, edad ,node.left)
        elif(carnet>node.Val):
            return self.Mod_Estudiante(carnet, DPI, nombre, carrera, correo, password, creditos, edad ,node.right)

    def AñadirAño(self, carnet, anio, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.años.insertar(anio)
            return "El dato es: " + node.Val
        elif(carnet<node.Val):
            return self.AñadirAño(carnet, anio, node.left)
        elif(carnet>node.Val):
            return self.AñadirAño(carnet, anio, node.right)

    def buscarmes(self, carnet, anio, mes, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.años.añadirmes(anio, mes, node.años.inicio)
        elif(carnet<node.Val):
            return self.buscarmes(carnet, anio, mes, node.left)
        elif(carnet>node.Val):
            return self.buscarmes(carnet, anio, mes, node.right)

    def buscarmatriz(self, carnet, anio, mes, dia, hora, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.años.buscarmes(anio, mes, dia, hora, node.años.inicio)
        elif(carnet<node.Val):
            return self.buscarmatriz(carnet, anio, mes, dia, hora, node.left)
        elif(carnet>node.Val):
            return self.buscarmatriz(carnet, anio, mes, dia, hora, node.right)

    def litareas(self, base, node, accion):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==base.carnet):
            node.años.tasklist(base, node.años.inicio, accion)
        elif(base.carnet<node.Val):
            return self.litareas(base, node.left, accion)
        elif(base.carnet>node.Val):
            return self.litareas(base, node.right, accion)

    def newAll(self, Tarea, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==Tarea.carnet):
            self.AñadirAño(Tarea.carnet, Tarea.direccionamiento[2], node)
            self.buscarmes(Tarea.carnet, Tarea.direccionamiento[2], Tarea.direccionamiento[1], node)
            self.buscarmatriz(Tarea.carnet, Tarea.direccionamiento[2], Tarea.direccionamiento[1], Tarea.direccionamiento[0], Tarea.hora, node)
            self.litareas(Tarea, node, "añadir")
            self.litareas(Tarea, node, "tarea")
        elif(Tarea.carnet<node.Val):
            return self.newAll(Tarea, node.left)
        elif(Tarea.carnet>node.Val):
            return self.newAll(Tarea, node.right)

    def RecuTarea(self, carnet, anio, mes, dia, hora, id, node, accion):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            return node.años.RecuTarea(anio, mes, dia, hora, id, accion)
        elif(carnet<node.Val):
            return self.RecuTarea(carnet, anio, mes, dia, hora, id, node.left, accion)
        elif(carnet>node.Val):
            return self.RecuTarea(carnet, anio, mes, dia, hora, id, node.right, accion)

    def buscarsemestre(self, carnet, anio, semestre, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.años.añadirsemestre(anio, semestre, node.años.inicio)
        elif(carnet<node.Val):
            return self.buscarsemestre(carnet, anio, semestre, node.left)
        elif(carnet>node.Val):
            return self.buscarsemestre(carnet, anio, semestre, node.right)

    def cursosEstudiante(self, carnet, anio, semestre, codigo, curso, creditos, pre, ob, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.años.añadirCurso(anio, semestre, codigo, curso, creditos, pre, ob, node.años.inicio)
        elif(carnet<node.Val):
            return self.cursosEstudiante(carnet, anio, semestre, codigo, curso, creditos, pre, ob, node.left)
        elif(carnet>node.Val):
            return self.cursosEstudiante(carnet, anio, semestre, codigo, curso, creditos, pre, ob, node.right)

    def graphTareas(self, carnet, año, mes, dia, hora, node):
        if(node==None):
            return "El arbol esta Vacio"
        elif(node.Val==carnet):
            node.años.graficarTarea(año, mes, dia, hora, node.años.inicio)
        elif(carnet<node.Val):
            return self.graphTareas(carnet, año, mes, dia, hora, node.left)
        elif(carnet>node.Val):
            return self.graphTareas(carnet, año, mes, dia, hora, node.right)

    def graficar(self, tipo, node):
        if(tipo=="encriptado"):
            file = open("FRONTEND/front/src/assets/ArbolAVLEncrypt.dot", 'w')
            file.write("digraph G { \n")
            file.write("rankdir=TB; \n")
            file.write("node [shape = record, color=black , style=filled, fillcolor=gray93];\n")        
            file.write(self.graficadoraEncrypt(node))
            file.write("} \n")
            file.close()
            os.system("dot -Tpng FRONTEND/front/src/assets/ArbolAVLEncrypt.dot -o FRONTEND/front/src/assets/ArbolAVLEncrypt_Alumnos.png")
            #os.startfile("ArbolAVLEncrypt_Alumnos.png")
        elif(tipo=="decriptado"):
            file = open("FRONTEND/front/src/assets/ArbolAVLDecrypt.dot", 'w')
            file.write("digraph G { \n")
            file.write("rankdir=TB; \n")
            file.write("node [shape = record, color=black , style=filled, fillcolor=gray93];\n")        
            file.write(self.graficadoraDecrypt(node))
            file.write("} \n")
            file.close()
            os.system("dot -Tpng FRONTEND/front/src/assets/ArbolAVLDecrypt.dot -o FRONTEND/front/src/assets/ArbolAVLDecrypt_Alumnos.png")
            #os.startfile("FRONTEND/front/src/assets/ArbolAVLDecrypt_Alumnos.png")

    def graficadoraEncrypt(self, node):
        cadena=""
        if((node.left==None) & (node.right==None)):
            cadena = "nodo"+str(node.Val)+"[ label=\""+"\\n Carnet: "+self.recortar(str(node.Carnet))+"\\n DPI: "+self.recortar(str(node.Identificacion))+"\\n Nombre: "+self.recortar(str(node.Nombre))+"\\n Carrera: "+self.recortar(str(node.Carrera))+"\\n Correo: "+self.recortar(str(node.Correo))+"\\n Password: "+self.recortar(str(node.Password))+"\\n Creditos: "+self.recortar(str(node.Creditos))+"\\n Edad: "+self.recortar(str(node.Edad))+"\"]; \n"
        else:
            cadena="nodo"+str(node.Val)+" [ label =\"<C0>| Carnet: "+self.recortar(str(node.Carnet))+"\\n DPI: "+self.recortar(str(node.Identificacion))+"\\n Nombre: "+self.recortar(str(node.Nombre))+"\\n Carrera: "+self.recortar(str(node.Carrera))+"\\n Correo: "+self.recortar(str(node.Correo))+"\\n Password: "+self.recortar(str(node.Password))+"\\n Creditos: "+self.recortar(str(node.Creditos))+"\\n Edad: "+self.recortar(str(node.Edad))+"|<C1>\"];\n"
        
        if(node.left!=None):
            cadena = cadena + self.graficadoraEncrypt(node.left)+"nodo"+str(node.Val)+":C0->nodo"+str(node.left.Val)+"\n"
        if(node.right!=None):
            cadena = cadena + self.graficadoraEncrypt(node.right)+"nodo"+str(node.Val)+":C1->nodo"+str(node.right.Val)+"\n"
        
        return cadena

    def graficadoraDecrypt(self, node):
        cadena=""
        if((node.left==None) & (node.right==None)):
            cadena = "nodo"+str(node.Val)+"[ label=\""+"\\n Carnet: "+keygen.decrypt(node.Carnet).decode()+"\\n DPI: "+ keygen.decrypt(node.Identificacion).decode()+"\\n Nombre: "+keygen.decrypt(node.Nombre).decode() +"\\n Carrera: "+keygen.decrypt(node.Carrera).decode() +"\\n Correo: "+keygen.decrypt(node.Correo).decode() +"\\n Password: "+keygen.decrypt(node.Password).decode() +"\\n Creditos: "+keygen.decrypt(node.Creditos).decode() +"\\n Edad: "+keygen.decrypt(node.Edad).decode() +"\"]; \n"
        else:
            cadena="nodo"+str(node.Val)+" [ label =\"<C0>| Carnet: "+keygen.decrypt(node.Carnet).decode()+"\\n DPI: "+ keygen.decrypt(node.Identificacion).decode()+"\\n Nombre: "+keygen.decrypt(node.Nombre).decode() +"\\n Carrera: "+keygen.decrypt(node.Carrera).decode() +"\\n Correo: "+keygen.decrypt(node.Correo).decode() +"\\n Password: "+keygen.decrypt(node.Password).decode() +"\\n Creditos: "+keygen.decrypt(node.Creditos).decode() +"\\n Edad: "+keygen.decrypt(node.Edad).decode() +"|<C1>\"];\n"
        
        if(node.left!=None):
            cadena = cadena + self.graficadoraDecrypt(node.left)+"nodo"+str(node.Val)+":C0->nodo"+str(node.left.Val)+"\n"
        if(node.right!=None):
            cadena = cadena + self.graficadoraDecrypt(node.right)+"nodo"+str(node.Val)+":C1->nodo"+str(node.right.Val)+"\n"
        
        return cadena

    def recortar(self, dato):
        da = list(dato)
        dato = ""
        for i in range(16):
            dato += da[i]
        return dato