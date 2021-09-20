from ESTRUCTURAS_.ARBOLB_.NodoPuntero import NodoPuntero

class ListaPuntero:

    def __init__(self):
        self.Primero=None
        self.Ultimo=None
        self.Cuenta=0
    
    def estaVacio(self):
        return (self.Primero==None)
    
    def InsertarPuntero(self, puntero):
        nuevo= NodoPuntero(puntero)
        if(self.Cuenta<5):
            if(self.estaVacio()):
                self.Primero=nuevo
                self.Ultimo=self.Primero
            else:
                self.Ultimo.setSiguienteP(nuevo)
                nuevo.setAnteriorP(self.Ultimo)
                self.Ultimo=nuevo
            self.Cuenta+=1

    def InsertarPunteroP(self, pagina, posicion):
        aux=self.Primero
        while(posicion!=0):
            posicion-=1
            aux=aux.getSiguienteP()
        aux.setPuntero(pagina)
    
    def DevolverPuntero(self, posicion):
        aux=self.Primero
        while(posicion!=0):
            posicion-=1
            aux=aux.getSiguienteP()
        return aux
    
    def getPrimero(self):
        return self.Primero

    def setPrimero(self, Primero):
        self.Primero = Primero

    def getCuenta(self):
        return self.Cuenta

    def setCuenta(self, Cuenta):
        self.Cuenta = Cuenta