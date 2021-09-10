import NodoArbolAVL

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.tamaño = 0
    
    def insertarNodo(Nodo):
        if self.raiz is None:
            self.raiz = Nodo
            self.raiz.tamaño = 0
            self.tamaño = 1
        else:
            new_node = None
            node_actual = self.raiz

            while True:
                if node_actual is not None:
                    new_node = node_actual

                    if Nodo.Carnet < node_actual.Carnet:
                        node_actual = node_actual.izquierda
                    else:
                        node_actual = node_actual.derecha
                else:
                    Nodo.tamaño = new_node.tamaño
                    new_node.tamaño +=1
                    if Nodo.Carnet < new_node.Carnet:
                        new_node = None
                    else:
                        new_node.derecha = None
                    self.balaceo(Nodo)
                    self.tamaño +=1
                    break

    def balaceo(self, Nodo):
         n = Nodo

         while n is not None:
            alto_derecha = n.tamaño
            alto_izquierda = n.tamaño

            if n.derecha is not None:
                alto_derecha = n.derecha.tamaño

            if abs(alto_izquierda - alto_derecha) > 1:
                if alto_izquierda > alto_derecha:
                    izquierda_pequeño = n.izquierda
                    if izquierda_pequeño is not None:
                        h_derecha = (izquierda_pequeño.derecha.tamaño
                                    if (izquierda_pequeño.derecha is not None) else 0)
                        h_left = (izquierda_pequeño.izquierda.tamaño
                                    if (izquierda_pequeño.izquierda is not None) else 0)
                    if (h_left > h_right):
                        self.rotar_izquierda(n)
                        break
                    else:
                        self.rote_doble_derecha(n)
                        break
                else:
                    derecha_pequeña = n.derecha
                    if derecha_pequeña is not None:
                        h_right = (derecha_pequeña.derecha.tamaño
                            if (derecha_pequeña.derecha is not None) else 0)
                        h_left = (derecha_pequeña.izquierda.tamaño
                            if (derecha_pequeña.izquierda is not None) else 0)
                    if (h_left > h_right):
                        self.rote_doble_izquierda(n)
                        break
                    else:
                        self.rotar_derecha(n)
                        break
            n = n.padre

    def rotar_izquierda(self, node):
        aux = node.padre.Carnet
        node.padre.Carnet = node.Carnet
        node.padre.derecha = Node(aux)
        node.padre.derecha.tamaño = node.padre.tamaño + 1
        node.padre.izquierda = node.derecha

    def rotar_derecha(self, node):
        aux = node.padre.Carnet
        node.padre.Carnet = node.Carnet
        node.padre.izquierda = Node(aux)
        node.padre.izquierda.tamaño = node.padre.tamaño + 1
        node.padre.derecha = node.derecha

    def rote_doble_izquierda(self, node):
        self.rotar_derecha(node.getRight().getRight())
        self.rotar_izquierda(node)

    def rote_doble_derecha(self, node):
        self.rotar_izquierda(node.getLeft().getLeft())
        self.rotar_derecha(node)

    def empty(self):
        if self.raiz is None:
            return True
        return False

    def preShow(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.izquierda)
            print(curr_node.Carnet, end=" ")
            self.preShow(curr_node.derecha)