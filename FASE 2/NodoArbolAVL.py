class NodoArbolAVL_:

    def __init__(self, Carnet, Identificacion, Nombre, Carrera, Correo, Password, Creditos, Edad):
        self.Carnet = Carnet
        self.Identificacion = Identificacion
        self.Nombre = Nombre
        self.Carrera = Carrera
        self.Correo = Correo
        self.Password = Password
        self.Creditos = Creditos
        self.años = None
        self.Edad = Edad
        self.padre = None
        self.left = None
        self.right = None
        self.height = 0