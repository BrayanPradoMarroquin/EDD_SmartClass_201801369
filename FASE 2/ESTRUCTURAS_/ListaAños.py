from ESTRUCTURAS_.Nodoaños import Años

class ListaAños_():
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, node):
        nuevo = Años(node)
        if self.inicio==None:    
            self.inicio = nuevo
            self.final = self.inicio
        else:
            cont = self.buscaranio(node)
            if cont==False:
                self.final.siguiente = nuevo
                nuevo.atras = self.final
                ultimo = nuevo
    
    def buscaranio(self, node):
        actual = self.inicio
        cond = False
        while (actual!=None) & (cond==False):
            if (actual.anio!=node):
                actual = actual.siguiente
            else:
                cond = True
        
        if (actual==None):
            return False
        elif (actual.anio==node):
            return True

    def añadirmes(self, año, mes, node):
        cond= False
        while (node!=None) & (cond==False):
            if(node.anio!=año):
                node = node.siguiente
            else:
                node.mese.insertar(mes)
                cond = True
        
