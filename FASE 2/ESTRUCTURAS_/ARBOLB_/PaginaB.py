from ESTRUCTURAS_.ARBOLB_.ListaPuntero import ListaPuntero
from ESTRUCTURAS_.ARBOLB_.ListaDoble import ListaDoble

class PaginaB:
    def __init__(self):
        self.Cuenta=0
        self.maxClaves=0
        self.punteros= ListaPuntero()
        self.datos= ListaDoble()

        for i in range(1,6):
            if(i!=4):
                self.datos.InsertarNodoD("", None, None, None, None)
            self.punteros.InsertarPuntero(None)
        self.maxClaves=5

    def paginaLlena(self):
        return(self.Cuenta==self.maxClaves-1)

    def paginaCasiLLena(self):
        return(self.Cuenta==self.maxClaves/2)
    
    def getCuenta(self):
        return self.Cuenta

    def setCuenta(self, Cuenta):
        self.Cuenta = Cuenta

    def getMaxClaves(self):
        return self.maxClaves

    def setMaxClaves(self, maxClaves):
        self.maxClaves = maxClaves
    
    def getCodigo(self, posicion):
        return self.datos.DevolverDato(posicion).getCodigo()
    
    def setCodigo(self, posicion, codigo):
        self.datos.InsertarDato(codigo, posicion)
    
    def getPais(self, posicion):
        return self.datos.DevolverDato(posicion).getPais()
    
    def setPais(self, posicion, pais):
        self.datos.DevolverDato(posicion).setPais(pais)

    def getCreditos(self, posicion):
        return self.datos.DevolverDato(posicion).getCreditos()

    def setCreditos(self, posicion, creditos):
        self.datos.DevolverDato(posicion).setCreditos(creditos)
    
    def getPrerequisitos(self, posicion):
        return self.datos.DevolverDato(posicion).getPrerequisitos()

    def setPrerequisitos(self, posicion, pre):
        self.datos.DevolverDato(posicion).setPrerequisitos(pre)

    def getObligatorio(self, posicion):
        return self.datos.DevolverDato(posicion).getObligatorio()

    def setObligatorio(self, posicion, pre):
        self.datos.DevolverDato(posicion).setObligatorio(pre)

    def getApuntador(self, posicion):
        return self.punteros.DevolverPuntero(posicion).getPuntero()
    
    def setApuntador(self, posicion, puntero):
        self.punteros.InsertarPunteroP(puntero, posicion)

