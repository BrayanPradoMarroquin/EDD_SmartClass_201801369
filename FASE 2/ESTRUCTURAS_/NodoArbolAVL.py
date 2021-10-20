from ESTRUCTURAS_.ListaAños import ListaAños_

class NodoArbolAVL_:
##---------------- aqui se agrego un validador de carnet ------------------------------------------------
    def __init__(self, val, Carnet, Identificacion, Nombre, Carrera, Correo, Password, Creditos, Edad):
        self.Val = val
        self.Carnet = Carnet
        self.Identificacion = Identificacion
        self.Nombre = Nombre
        self.Carrera = Carrera
        self.Correo = Correo
        self.Password = Password
        self.Creditos = Creditos
        self.años = ListaAños_()
        self.Edad = Edad
        self.padre = None
        self.left = None
        self.right = None
        self.height = 0