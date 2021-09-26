from ESTRUCTURAS_.ListaTareas import ListTareas

class NodoCab:
    def __init__(self, num):
        self.num = num
        self.siguiente = None
        self.antes = None
        self.arriba = None
        self.abajo = None

class NodoData:
    def __init__(self, dato, fila, columna):
        self.data = dato
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
        self.tareas = ListTareas()

class Listacabecera:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, num):
        if(self.buscarcabecera(num)==False):
            nuevo = NodoCab(num)
            if self.inicio == None:
                self.inicio = nuevo
                self.final = self.inicio
            else:
                if(self.inicio.num==self.final.num):
                    if (num>self.inicio.num):
                        self.final.siguiente = nuevo
                        nuevo.antes = self.final
                        self.final = nuevo
                    elif(num<self.inicio.num):
                        nuevo.siguiente = self.inicio
                        self.inicio.antes = nuevo
                        self.inicio = nuevo
                else:
                    cond = False
                    actual = self.inicio
                    while(actual!=None) & (cond==False):
                        if(num==1):
                            nuevo.siguiente = self.inicio
                            self.inicio.antes = nuevo
                            self.inicio = nuevo
                            cond=True
                        elif(num>actual.num):
                            actual = actual.siguiente
                        else:
                            nuevo.antes = actual.antes
                            actual.antes.siguiente = nuevo
                            actual.antes = nuevo
                            nuevo.siguiente = actual
                            cond = True

                    if(actual==None) & (cond==False):
                        self.final.siguiente = nuevo
                        nuevo.antes = self.final
                        self.final = nuevo
        
    def imprimir(self):
        actual = self.inicio
        while(actual!=None):
            print(actual.num)
            actual = actual.siguiente

    def buscarcabecera(self, data):
        actual = self.inicio
        cond=False
        if(self.inicio!=None):
            while(actual!=None) & (cond==False):
                if(actual.num==data):
                    return True
            return False
        else:
            return False

class ListaData:
    def __init__(self):
        self.head = None
        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None

    def insertar(self, posX, posY, listaX, listaY, nuevoNodo):
        if(self.valtarea(listaX, listaY, posX, posY)==False):
            lTemporalX = listaX.inicio
            lTemporalY = listaY.inicio

            while lTemporalX.num != posX:
                lTemporalX = lTemporalX.siguiente
            listaX = lTemporalX

            while lTemporalY.num != posY:
                lTemporalY = lTemporalY.siguiente
            listaY = lTemporalY

            if listaX and listaY:
                tempUltimoX = listaX
                tempUltimoY = listaY
                while tempUltimoX.abajo != None:
                    tempUltimoX = tempUltimoX.abajo
                while tempUltimoY.abajo != None:
                    tempUltimoY = tempUltimoY.abajo
                tempUltimoX.abajo = nuevoNodo
                tempUltimoY.abajo = nuevoNodo
                nuevoNodo.arriba = tempUltimoX
                nuevoNodo.izquierda = tempUltimoY
            else:
                listaX = nuevoNodo
                listaX.abajo = nuevoNodo
                listaY = nuevoNodo
                listaY.abajo= nuevoNodo

    def mostrar(self, listaX, listaY, posX, posY):
        listaCabeceraX = listaX.inicio
        listaCabeceraY = listaY.inicio

        while listaCabeceraX.num != int(posX):
            listaCabeceraX = listaCabeceraX.siguiente
        print('La cabecera en x es ', listaCabeceraX.num)

        while listaCabeceraY.num != int(posY):
            listaCabeceraY = listaCabeceraY.siguiente
        print('La cabecera en y es ', listaCabeceraY.num)

        temp = listaCabeceraX.abajo
        while temp != None:
            temp = temp.abajo
        temp = listaCabeceraY.abajo
        cond = False
        while (temp != None) & (cond==False):
            if(temp.fila==posX) & (temp.columna==posY):
                print(temp.data, end='->')
                cond = True
            else:
                temp = temp.abajo

    def buscarTarea(self, listaX, listaY, posX, posY, node):
        listaCabeceraX = listaX.inicio
        listaCabeceraY = listaY.inicio

        while listaCabeceraX.num != posX:
            listaCabeceraX = listaCabeceraX.siguiente
        print('La cabecera en x es ', listaCabeceraX.num)

        while listaCabeceraY.num != posY:
            listaCabeceraY = listaCabeceraY.siguiente
        print('La cabecera en y es ', listaCabeceraY.num)

        temp = listaCabeceraX.abajo
        while temp != None:
            temp = temp.abajo
        temp = listaCabeceraY.abajo
        cond = False
        while (temp != None) & (cond==False):
            if(temp.fila==posY) & (temp.columna==posX):
                temp.data +=1
                node.id = temp.data
                temp.tareas.insertar(node)
                
                cond = True
            else:
                temp = temp.abajo

    def RecuTarea(self, listaX, listaY, posX, posY, id, accion):
        listaCabeceraX = listaX.inicio
        listaCabeceraY = listaY.inicio

        while listaCabeceraX.num != posX:
            listaCabeceraX = listaCabeceraX.siguiente
        print('La cabecera en x es ', listaCabeceraX.num)

        while listaCabeceraY.num != posY:
            listaCabeceraY = listaCabeceraY.siguiente
        print('La cabecera en y es ', listaCabeceraY.num)

        temp = listaCabeceraX.abajo
        while temp != None:
            temp = temp.abajo
        temp = listaCabeceraY.abajo
        cond = False
        while (temp != None) & (cond==False):
            if(temp.fila==posY) & (temp.columna==posX):
                if(accion=="Obtener"):
                    return temp.tareas.buscartarea(id)
                    cond = True
                elif(accion=="Eliminar"):
                    return temp.tareas.Eliminar(id)
                    cond = True
            else:
                temp = temp.abajo

    def actualizarTarea(self, listaX, listaY, posX, posY, id, carnet, nombre, descripcion, materia, fecha, hora, status):
        listaCabeceraX = listaX.inicio
        listaCabeceraY = listaY.inicio

        while listaCabeceraX.num != posX:
            listaCabeceraX = listaCabeceraX.siguiente
        print('La cabecera en x es ', listaCabeceraX.num)

        while listaCabeceraY.num != posY:
            listaCabeceraY = listaCabeceraY.siguiente
        print('La cabecera en y es ', listaCabeceraY.num)

        temp = listaCabeceraX.abajo
        while temp != None:
            temp = temp.abajo
        temp = listaCabeceraY.abajo
        cond = False
        while (temp != None) & (cond==False):
            if(temp.fila==posY) & (temp.columna==posX):
                return temp.tareas.actualizarTarea(id, carnet, nombre, descripcion, materia, fecha, hora, status)
                cond = True
            else:
                temp = temp.abajo

    def graficarTareas(self, listaX, listaY, posX, posY):
        listaCabeceraX = listaX.inicio
        listaCabeceraY = listaY.inicio

        while listaCabeceraX.num != posX:
            listaCabeceraX = listaCabeceraX.siguiente
        print('La cabecera en x es ', listaCabeceraX.num)

        while listaCabeceraY.num != posY:
            listaCabeceraY = listaCabeceraY.siguiente
        print('La cabecera en y es ', listaCabeceraY.num)

        temp = listaCabeceraX.abajo
        while temp != None:
            temp = temp.abajo
        temp = listaCabeceraY.abajo
        cond = False
        while (temp != None) & (cond==False):
            if(temp.fila==posY) & (temp.columna==posX):
                temp.tareas.graficar()
                cond = True
            else:
                temp = temp.abajo

    def valtarea(self, listaX, listaY, posX, posY):
        listaCabeceraX = listaX.inicio
        listaCabeceraY = listaY.inicio

        while listaCabeceraX.num != posX:
            listaCabeceraX = listaCabeceraX.siguiente
        print('La cabecera en x es ', listaCabeceraX.num)

        while listaCabeceraY.num != posY:
            listaCabeceraY = listaCabeceraY.siguiente
        print('La cabecera en y es ', listaCabeceraY.num)

        temp = listaCabeceraX.abajo
        while temp != None:
            temp = temp.abajo
        temp = listaCabeceraY.abajo
        cond = False
        while (temp != None) & (cond==False):
            if(temp.fila==posY) & (temp.columna==posX):
                return True
        return False