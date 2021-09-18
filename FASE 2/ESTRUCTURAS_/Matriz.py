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
        nuevo = NodoCab(num)
        if self.inicio == None:
            self.inicio = nuevo
            self.final = self.inicio
        else:
            if(self.inicio.num==self.final.num):
                self.final.siguiente = nuevo
                nuevo.antes = self.final
                self.final = nuevo
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

class ListaData:
    def __init__(self):
        self.head = None
        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None

    def insertar(self, posX, posY, listaX, listaY, nuevoNodo):
        lTemporalX = listaX.inicio
        lTemporalY = listaY.inicio

        while lTemporalX.num != int(posX):
            lTemporalX = lTemporalX.siguiente
        listaX = lTemporalX

        while lTemporalY.num != int(posY):
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