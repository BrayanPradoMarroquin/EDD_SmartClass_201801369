from ESTRUCTURAS_.Nodoaños import Años

class ListaAños_():
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, node):
        nuevo = Años(node)
        if self.inicio==None:    
            self.inicio = nuevo
            self.final = self.inicio
        else:
            cont = self.buscaranio(node)
            if cont==False:
                self.final.siguiente = nuevo
                nuevo.atras = self.final
                ultimo = nuevo
    
    def buscaranio(self, node):
        actual = self.inicio
        cond = False
        while (actual!=None) & (cond==False):
            if (actual.anio!=node):
                actual = actual.siguiente
            else:
                cond = True
        
        if (actual==None):
            return False
        elif (actual.anio==node):
            return True

    def añadirmes(self, año, mes, node):
        cond= False
        while (node!=None) & (cond==False):
            if(node.anio!=año):
                node = node.siguiente
            else:
                node.mese.insertar(mes)
                cond = True
        
    def añadirsemestre(self, año, semestre, node):
        if ((semestre=='1') | (semestre=='2')):
            cond = False
            while(node!=None) & (cond==False):
                if(node.anio!=año):
                    node = node.siguiente
                else:
                    node.semestre.insertar(semestre)
                    cond = True

    def añadirCurso(self, anio, semestre, codigo, curso, creditos, pre, ob, node):
        if ((semestre=='1') | (semestre=='2')):
            cond = False
            while(node!=None) & (cond==False):
                if(node.anio!=anio):
                    node = node.siguiente
                else:
                    node.semestre.insertarCurso(semestre, codigo, curso, creditos, pre, ob, node.semestre)
                    cond = True

    def buscarmes(self, año, mes, dia, hora, node):
        cond=False
        while(node!=None) & (cond==False):
            if(node.anio!=año):
                node = node.siguiente
            else:
                node.mese.añadircabeceras(mes, dia, hora, node.mese.inicio)
                cond=True
    
    def RecuTarea(self, año, mes, dia, hora, id):
        actual = self.inicio
        while(actual!=None):
            if(actual.anio!=año):
                actual = actual.siguiente
            else:
                return actual.mese.RecuTarea(mes, dia, hora, id)

    def actualizarTarea(self, año, mes, dia, hora, id, carnet, nombre, descripcion, materia, fecha, status):
        actual = self.inicio
        while(actual!=None):
            if(actual.anio!=año):
                actual = actual.siguiente
            else:
                return actual.mese.actualizarTarea(mes, dia, hora, id, carnet, nombre, descripcion, materia, fecha, hora, status)    

    def graficarTarea(self, año, mes, dia, hora, node):
        cond=False
        while(node!=None) & (cond==False):
            if(node.anio!=año):
                node = node.siguiente
            else:
                node.mese.graficaTareas(mes, dia, hora, node.mese.inicio)
                cond=True

    def tasklist(self, base, node, accion):
        cond=False
        while(node!=None) & (cond==False):
            if(node.anio!=base.direccionamiento[2]):
                node = node.siguiente
            else:
                if(accion=="añadir"):
                    node.mese.añadirtask(base, node.mese.inicio)
                    cond=True
                elif(accion=="tarea"):
                    node.mese.Taskañadir(base, node.mese.inicio)
                    cond=True
                elif(accion=="new"):
                    node.mese.NewTarea(base, node.mese.inicio)
                    cond=True