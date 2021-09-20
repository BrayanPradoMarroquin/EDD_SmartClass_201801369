class NodoDoble:
    def __init__(self, codigo, pais, creditos, Prerequisitos, Obligatorio):
        self.codigo = codigo
        self.pais=pais
        self.creditos = creditos
        self.Prerequisitos = Prerequisitos
        self.Obligatorio = Obligatorio
        self.Siguiente=None
        self.Anterior=None

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais

    def getCreditos(self):
        date = self.creditos
        return date

    def setCreditos(self, creditos):
        self.creditos = creditos

    def getPrerequisitos(self):
        return self.Prerequisitos

    def setPrerequisitos(self, Prerequisitos):
        self.Prerequisitos = Prerequisitos

    def getObligatorio(self):
        return self.Obligatorio

    def setObligatorio(self, Obligatorio):
        self.Obligatorio = Obligatorio

    def getSiguiente(self):
        return self.Siguiente

    def setSiguiente(self, Siguiente):
        self.Siguiente = Siguiente

    def getAnterior(self):
        return self.Anterior

    def setAnterior(self, Anterior):
        self.Anterior = Anterior