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

class Node:
    def __init__(self, label):
            self.label = label
            self.parent = None
            self.left = None
            self.right = None
            self.height = 0

class AVL:
    def __init__(self):
        self.root = None

    def max(self, v1, v2):
        if v1>v2:
            return v1
        else:
            return v2

    def tamaño(self, node):
        if node is not None:
            return node.height
        return -1

    def insert(self, value):
        self.root = self.insert_interno(value, self.root)

    def insert_interno(self, value, root):
        if root is None:
            return value
        else:
            if value.Carnet< root.Carnet:
                root.left = self.insert_interno(value, root.left)
                if self.tamaño(root.right) - self.tamaño(root.left) == -2:
                    if value.Carnet < root.left.Carnet:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif value.Carnet > root.Carnet:
                root.right = self.insert_interno(value, root.right)
                if self.tamaño(root.right) - self.tamaño(root.left) == 2:
                    if value.Carnet > root.right.Carnet:
                        root = self.RD(root)
                    else:
                        root = self.RDD(root)
            else:
                root.label = value
        
        root.height = self.max(self.tamaño(root.left), self.tamaño(root.right)) + 1
        return root


    def RI(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        node.height = self.max(self.tamaño(node.left), self.tamaño(node.right)) + 1
        aux.height = self.max(self.tamaño(aux.left), self.tamaño(aux.right)) + 1
        return aux

    def RD(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        node.height = self.max(self.tamaño(node.left), self.tamaño(node.right)) + 1
        aux.height = self.max(self.tamaño(aux.left), self.tamaño(aux.right)) + 1
        return aux

    def RDI(self, node):
        node.left = self.RD(node.left)
        return self.RI(node)

    def RDD(self, node):
        node.right = self.RI(node.right)
        return self.RD(node)

    def preShow(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.left)
            print(curr_node.label, end=" ")
            self.preShow(curr_node.right)
    

if __name__ == '__main__':
    t = AVL()
    t.insert(NodoArbolAVL_(201801369, 2995454660101, "Brayan", "Yisus", "te quiero nene", 123650, 112, 22))
    t.insert(NodoArbolAVL_(201801627, 2995454660101, "Risas", "Yisus", "te quiero nene", 123650, 112, 22))
    t.insert(NodoArbolAVL_(201801603, 2995454660101, "Ricardo", "Yisus", "te quiero nene", 123650, 112, 22))
    t.insert(NodoArbolAVL_(201801146, 2995454660101, "Coti", "Yisus", "te quiero nene", 123650, 112, 22))
    t.preShow(t.root)