class NodoArista:
    def __init__(self, codigo, curso, creditos, pre):
        self.codigo = codigo
        self.curso = curso
        self.creditos = creditos
        self.pre = pre
        self.siguiente = None

class ListaAristas:
    def __init__(self):
        self.inicio = None

    def agregar(self, Nodo):
        if (self.inicio==None):
            self.inicio = Nodo
        else:
            Nodo.siguiente = self.inicio
            self.inicio = Nodo

    def imprimir(self):
        actual = self.inicio
        while(actual!=None):
            print("El curso con codigo: "+actual.curso)
            print("Y prerrequisitos")
            for pre in actual.pre:
                print(pre)
            print("\n")
            actual = actual.siguiente

Grafo = ListaAristas()
Grafo.agregar(NodoArista(103, "Matematica Basica 2", [101]))
Grafo.agregar(NodoArista(101, "Matematica Basica 1", []))
Grafo.imprimir()