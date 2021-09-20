from ESTRUCTURAS_.ARBOLB_.NodoDoble import NodoDoble

class ListaDoble:
    def __init__(self):
        self.Cuenta=0
        self.Primero=None
        self.Ultimo=None

    def estaVacio(self):
        return (self.Primero==None)

    def InsertarNodoD(self, codigo, pais, creditos, Prerequisitos, Obligatorio):
        nuevo= NodoDoble(codigo, pais, creditos, Prerequisitos, Obligatorio)
        if(self.Cuenta<4):
            if(self.estaVacio()):
                self.Primero=nuevo
                self.Ultimo=self.Primero
            else:
                self.Ultimo.setSiguiente(nuevo)
                nuevo.setAnterior(self.Ultimo)
                self.Ultimo=nuevo
            self.Cuenta+=1
        else:
            print("Ya se ha superado el tamaño")
    
    def InsertarDato(self, codigo, posicion):
        aux=self.Primero
        while(posicion!=0):
            posicion-=1
            aux=aux.getSiguiente()
        aux.setCodigo(codigo)
    
    def DevolverDato(self, posicion):
        aux=self.Primero
        while(posicion!=0):
            posicion-=1
            aux=aux.getSiguiente()
        return aux
    
    def MostrarDatos(self):
        aux=self.Primero
        while(aux!=None):
            print("Dato " + aux.getCodigo())
            aux=aux.getSiguiente()