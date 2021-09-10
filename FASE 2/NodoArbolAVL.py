class NodoArbolAVL:

    def __init__(self, Carnet, Identificacion, Nombre, Carrera, Correo, password, Creditos, Edad):
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
        self.izquierda = None
        self.derecha = None
        self.tamaño = 0

    @property
    def right(self):
        return self.derecha

    @right.setter
    def right(self, node):
        if node is not None:
            node.padre = self
            self.derecha = node

    @property
    def left(self):
        return self.izquierda

    @left.setter
    def left(self, node):
        if node is not None:
            node.padre = self
            self.izquierda = node

    @property
    def parent(self):
        return self.padre

    @parent.setter
    def parent(self, node):
        if node is not None:
            self.padre = node
            self.tamaño = self.padre.tamaño + 1
        else:
            self.tamaño = 0
