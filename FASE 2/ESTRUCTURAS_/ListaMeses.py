from ESTRUCTURAS_.NodoMeses import NodoMes

class Meses:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, mes):
        nuevo = NodoMes(mes)
        if self.inicio == None:
            self.inicio = nuevo
            self.final  = self.inicio
        else:
            cont = self.buscarmes(mes)
            if cont==False:
                self.final.siguiente = nuevo
                nuevo.atras = self.final
                ultimo = nuevo
    
    def buscarmes(mes):
        actual = self.inicio
        cond = False
        while (actual!=None) & (cond==False):
            if (actual.mes!=mes):
                actual = actual.siguiente
            else:
                cond = True
        
        if (actual==None):
            return False
        elif (actual.mes==mes):
            return True