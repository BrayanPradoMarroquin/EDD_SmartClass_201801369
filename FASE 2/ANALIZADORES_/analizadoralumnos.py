import re
from ESTRUCTURAS_.NodoArbolAVL import NodoArbolAVL_ 
import alumnos
from NodoTask import Tareas

valor=""
flagId=False
flagCadena=False
flagNumero=False
flagAlumnos=False
flagTask=False
Estado=0
temp=None
tablaSimbolos = []
tablaSimbolosTask=[]
listaTask = []
ma = []

class Simbolo:

    def __init__(self,token,lexema):
        self.token = token 
        self.lexema = lexema 

def alumno(ruta):
    data = open(ruta, "r", encoding='utf-8')
    texto = data.read()
    data.close()
    listData = texto.split("\n")
    condicionuser=False
    condiciontask=False
    for li in listData:
        if re.match("[^\t]*¿element type=\"user\"?", li):
            print(li)
            condicionuser=True
            condiciontask=False
        elif re.match("[^\t]*¿element type=\"task\"?", li):
            if (condicionuser==True):
                condicionuser=False
                condiciontask=True
        elif (condicionuser==True):
            analizador_Alumno(li)
        elif (condiciontask):
            analizador_Task(li)

#------------------Area de los Alumnos para ingresar ----------------------------------------

def isletter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122)

def isnumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)

def expresionId(c):
    global valor,columna,fila,flagId    
    if isletter(c):
        valor += c
        return
    elif ord(c) == 32:
        tablaSimbolos.append(Simbolo("ID",valor))
        valor = ""
        flagId = False
    elif ord(c) == 61:
        tablaSimbolos.append(Simbolo("ID",valor))
        valor = ""
        flagId = False
    elif ord(c) == 63:
        tablaSimbolos.append(Simbolo("ID",valor))
        valor = ""
        flagId = False

def expresionCadena(c):
    global valor,columna,fila,flagCadena 

    if ord(c) == 34: 
        tablaSimbolos.append(Simbolo("CADENA",valor))
        valor = ""
        flagCadena = False
        return; 
    
    valor += c

def expresionNumero(c):
    global columna,fila,flagNumero,valor
    if isnumber(c):
        valor += c
        return 

    tablaSimbolos.append(Simbolo("NUMERO",valor))
    valor = ""
    flagNumero = False

def analizador_Alumno(c):
    global valor, flagId, flagCadena, flagNumero
    flagCadena = False
    flagNumero = False
    flagId = False
    caracteres = list(c)
    for i in caracteres:
        ca = ord(i)
        if flagId:
            expresionId(i)
        elif flagCadena:
            expresionCadena(i)
        elif flagNumero:
            expresionNumero(i)
        elif isletter(i):
            flagId=True
            valor=i
        elif isnumber(i):
            flagNumero=True
            valor=i
        elif ord(i)==34:
            flagCadena=True
        elif ord(i)==32:
            pass

def automataalumnos(li):
    global Estado, temp, flagAlumnos
    if Estado==0:
        if li.lexema=="Carnet":
            temp = NodoArbolAVL_(0, 0, 0, 0, 0, 0, 0, 0)
            Estado = 1
        elif li.lexema=="DPI":
            Estado = 3
        elif li.lexema=="Nombre":
            Estado = 4
        elif li.lexema=="Carrera":
            Estado = 5
        elif li.lexema=="Correo":
            Estado = 6
        elif li.lexema=="Password":
            Estado = 7
        elif li.lexema=="Creditos":
            Estado = 8
        elif li.lexema=="Edad":
            Estado = 9
    elif Estado==1:
        if li.token=="CADENA":
            temp.Carnet = li.lexema
            Estado = 2
    elif Estado==2:
        if li.lexema=="item":
            Estado=0
        elif li.lexema=="element":
            alumnos.Alumnos_.insert(temp)
            temp=None
            flagAlumnos=False
            Estado=0
    elif Estado==3:
        if li.token=="CADENA":
            temp.Identificacion = li.lexema
            Estado = 2
    elif Estado==4:
        if li.token=="CADENA":
            temp.Nombre = li.lexema
            Estado = 2
    elif Estado==5:
        if li.token=="CADENA":
            temp.Carrera = li.lexema
            Estado = 2
    elif Estado==6:
        if li.token=="CADENA":
            temp.Correo = li.lexema
            Estado = 2
    elif Estado==7:
        if li.token=="CADENA":
            temp.Password = li.lexema
            Estado = 2
    elif Estado==8:
        if li.token=="NUMERO":
            temp.Creditos = li.lexema
            Estado = 2
    elif Estado==9:
        if li.token=="NUMERO":
            temp.Edad = li.lexema
            Estado = 2

def sintac():
    global flagAlumnos
    for da in tablaSimbolos:
        if flagAlumnos:
            automataalumnos(da)
        elif da.lexema=="item":
            Estado=0
            flagAlumnos=True

#-------------------------------------Area de las Tareas para ingresar----------------------------------------

def expresionIdTask(c):
    global valor,columna,fila,flagId    
    if isletter(c):
        valor += c
        return
    elif ord(c) == 32:
        tablaSimbolosTask.append(Simbolo("ID",valor))
        valor = ""
        flagId = False
    elif ord(c) == 61:
        tablaSimbolosTask.append(Simbolo("ID",valor))
        valor = ""
        flagId = False
    elif ord(c) == 63:
        tablaSimbolosTask.append(Simbolo("ID",valor))
        valor = ""
        flagId = False

def expresionCadenaTask(c):
    global valor,columna,fila,flagCadena 

    if ord(c) == 34: 
        tablaSimbolosTask.append(Simbolo("CADENA",valor))
        valor = ""
        flagCadena = False
        return; 
    
    valor += c

def analizador_Task(c):
    global valor, flagId, flagCadena, flagNumero
    caracteres = list(c)
    flagCadena = False
    flagId = False
    for i in caracteres:
        ca = ord(i)
        if flagId:
            expresionIdTask(i)
        elif flagCadena:
            expresionCadenaTask(i)
        elif isletter(i):
            flagId=True
            valor=i
        elif ord(i)==34:
            flagCadena=True
        elif ord(i)==32:
            pass

def automataTask(li):
    global Estado, temp, flagTask, valor, ma
    if Estado==0:
        if li.lexema=="Carnet":
            Estado =1
            temp = Tareas(0, 0, 0, 0, 0, 0, 0)
        elif li.lexema=="Nombre":
            Estado=3
        elif li.lexema=="Descripcion":
            Estado=4
        elif li.lexema=="Materia":
            Estado=5
        elif li.lexema=="Fecha":
            Estado=6
        elif li.lexema=="Hora":
            Estado=7
        elif li.lexema=="Estado":
            Estado=8
    elif Estado==1:
        if li.token=="CADENA":
            temp.carnet = li.lexema
            Estado = 2
    elif Estado==2:
        if li.lexema=="item":
            Estado=0
        elif li.lexema=="element": 
            alumnos.Alumnos_.litareas(temp, alumnos.Alumnos_.root, "añadir")
            alumnos.Alumnos_.litareas(temp, alumnos.Alumnos_.root, "tarea")
            temp=None
            flagTask=False
            ma = []
            Estado=0
    elif Estado==3:
        if li.token=="CADENA":
            temp.nombre = li.lexema
            Estado = 2
    elif Estado==4:
        if li.token=="CADENA":
            temp.descripcion = li.lexema
            Estado = 2
    elif Estado==5:
        if li.token=="CADENA":
            temp.materia = li.lexema
            Estado = 2
    elif Estado==6:
        if li.token=="CADENA":
            temp.fecha = li.lexema
            Estado = 2
            valores = li.lexema.split('/')
            alumnos.Alumnos_.AñadirAño(temp.carnet, valores[2], alumnos.Alumnos_.root)
            alumnos.Alumnos_.buscarmes(temp.carnet, valores[2], valores[1], alumnos.Alumnos_.root)
            ma = valores
            data = ""
    elif Estado==7:
        if li.token=="CADENA":
            temp.hora = li.lexema
            alumnos.Alumnos_.buscarmatriz(temp.carnet, ma[2], ma[1], ma[0], temp.hora, alumnos.Alumnos_.root)
            temp.direccionamiento = ma
            Estado = 2
    elif Estado==8:
        if li.token=="CADENA":
            temp.status = li.lexema
            Estado = 2

def sintacT():
    global flagTask, Estado
    for da in tablaSimbolosTask:
        if flagTask:
            automataTask(da)
        elif da.lexema=="item":
            Estado=0
            flagTask=True
