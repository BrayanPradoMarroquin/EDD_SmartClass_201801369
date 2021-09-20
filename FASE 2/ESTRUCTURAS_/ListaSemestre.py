from ESTRUCTURAS_.NodoSemestre import Semestre

class ListSemestre:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, data):
        nuevo = Semestre(data)
        if self.inicio == None:
            self.inicio = nuevo
            self.final  = self.inicio
        else:
            cont = self.buscarsemestre(data)
            if cont==False:
                self.final.siguiente = nuevo
                nuevo.atras = self.final
                ultimo = nuevo
    
    def insertarCurso(self, semestre, codigo, curso, creditos, pre, ob, node):
        actual = self.inicio
        cond = False
        while (actual!=None) & (cond==False):
            if (actual.semestre!=semestre):
                actual = actual.siguiente
            else:
                node.cursos.InsertarDatos(codigo, curso, creditos, pre, ob)
                cond = True

    def buscarsemestre(self, data):
        actual = self.inicio
        cond = False
        while (actual!=None) & (cond==False):
            if (actual.semestre!=data):
                actual = actual.siguiente
            else:
                cond = True
        
        if (actual==None):
            return False
        elif (actual.semestre==data):
            return True