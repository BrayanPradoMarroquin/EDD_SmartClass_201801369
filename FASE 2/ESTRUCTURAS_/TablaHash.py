from ESTRUCTURAS_.ListaTareas import ListTareas
from NodoTask import Tareas
import os

primos = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

class NodoCont:
    def __init__(self, carnet):
        self.carnet = carnet
        self.anotaciones = ListTareas()

class TablaHash:
    def __init__(self, tamaño):
        self.Hash = None
        self.tamaño = tamaño
        self.minimo = 0
        self.agregados = 0
        self.iniciar()

    def iniciar(self):
        self.agregados = 0
        self.minimo = (self.tamaño/2)+0.5
        Newtable = [None]*self.tamaño

        self.Hash = Newtable

    def cargarInf(self, data, tit, des):
        posicion = self.FunHash(data)
        try:
            it1 = 0
            it2 = 0
            while(data!=self.Hash[posicion].carnet):
                if(self.Hash[posicion]!=None):
                    if(it1<4):
                        it1+=1   
                        posicion = self.ColsicionHash(data, posicion)
                        it2+=1
                    elif(posicion<self.tamaño-1) & (it1>=4):
                        posicion +=1
                    elif(posicion==self.tamaño-1):
                        posicion = 0
        
            self.Hash[posicion].anotaciones.insertar(Tareas(tit, des))
        except:
            print("El dato no existe")

    def BsucarId(self, carnet):
        for H in self.Hash:
            if(H==None):
                pass
            elif(H.carnet==carnet):
                return True
        return False

    def agregar(self, data):
        if(data!=None):
            if(self.BsucarId(data.carnet)==False):
                posicion = self.FunHash(data.carnet)
                it1 = 0
                it2 = 0
                if(posicion<self.tamaño):
                    while(self.Hash[posicion] != None):
                        if(it1<4):
                            it1+=1    
                            posicion = self.ColsicionHash(data.carnet, posicion)
                            it2+=1
                        elif(posicion<self.tamaño-1) & (it1>=4):
                            posicion +=1
                        elif(posicion==self.tamaño-1):
                            posicion = 0
                else:
                    posicion = 0

                self.Hash[posicion] = data
                self.agregados+=1
                self.rehashing()

    def FunHash(self,data):
        return int(data) % self.tamaño

    def ColsicionHash(self, data, i):
        return (int(data) +(i*i)) % self.tamaño

    def Divisibilidad(self, ta):
        for i in range(0,len(primos)):
            if (int(ta)==int(primos[i])):
                return primos[i+1]
                
    def rehashing(self):
        if(self.agregados >= self.minimo):
            copyarray = self.Hash

            tamañoAnterior = self.tamaño

            Mod = self.Divisibilidad(self.tamaño) 
            
            self.tamaño = Mod

            self.iniciar()

            for i in range(0,tamañoAnterior):
                if(copyarray[i] != -1):
                        self.agregar(copyarray[i])

    def imprimir(self):
        for i in range(0,len(self.Hash)):
            if(self.Hash[i]!=None):
                print(str(i)+" -> " + str(self.Hash[i].carnet))
            else:
                print(str(i)+" -> " + "No hay informacion")

    def graficar(self):
        cadena = ""
        file = open("FRONTEND/front/src/assets/TablaHash.dot", 'w')
        file.write("digraph G { \n")
        file.write("rankdir=LR; \n")
        cadena = 'struct1 [label=\"'        
        for ap in range(len(self.Hash)):
            if(self.Hash[ap]!=None) & (ap!=(self.tamaño-1)):
                cadena = cadena +"<f"+str(ap)+">"+str(self.Hash[ap].carnet)+"|"
            elif(ap==(self.tamaño-1)):
                if(self.Hash[ap]!=None):
                    cadena = cadena +"<f"+str(ap)+">"+str(self.Hash[ap].carnet)
                else:
                    cadena = cadena +"<f"+str(ap)+">"+"   "    
            else:
                cadena = cadena +"<f"+str(ap)+">"+"   "+"|"
        cadena = cadena + '\" shape=record fontsize=\"40\"]; \n'
        for ap in range(len(self.Hash)):
            if(self.Hash[ap]!=None):
                cadena += self.Hash[ap].anotaciones.graficar(ap)

        file.write(cadena)
        file.write("} \n")
        file.close()
        os.system("dot -Tpng FRONTEND/front/src/assets/TablaHash.dot -o FRONTEND/front/src/assets/TablaHash.png")
