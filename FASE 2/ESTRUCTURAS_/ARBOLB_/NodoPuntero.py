class NodoPuntero:
    
    def __init__(self, puntero):
        self.Puntero=puntero
        self.SiguienteP=None

    def getPuntero(self):
        return self.Puntero

    def setPuntero(self, Puntero):
        self.Puntero = Puntero

    def getSiguienteP(self):
        return self.SiguienteP

    def setSiguienteP(self, SiguienteP):
        self.SiguienteP = SiguienteP

    def getAnteriorP(self):
        return self.AnteriorP

    def setAnteriorP(self, AnteriorP):
        self.AnteriorP = AnteriorP