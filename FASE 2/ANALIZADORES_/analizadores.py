from io import open
import alumnos
import json
import ANALIZADORES_.Conex 
import hashlib

def cargar_datos_Pensum(ruta):
    archivo = open(ruta, 'r', encoding='utf-8')
    texto = archivo.read()
    expresion = analisis(texto)
    ejecutar = open('recuperadoPensum.json', 'w', encoding='utf-8')
    ejecutar.write(expresion)
    ejecutar.close()

    with open("recuperadoPensum.json", "r", encoding="utf-8") as f:
        cursos = json.load(f)
        for curso in cursos:
            print(curso.get('Codigo') + " -> " + curso.get('Nombre')+" -> "+str(curso.get("Creditos"))+" -> "+ curso.get("Prerequisitos")+" -> "+ str(curso.get("Obligatorio")))
            alumnos.Pensum.agregar(curso.get('Codigo'), curso.get('Nombre'), curso.get("Creditos"), curso.get("Prerequisitos"), curso.get("Obligatorio"))

def analisis(texto):
    cadena = ""
    condicion = False
    for i in texto:
        if(i=="["):
            condicion=True
            cadena+=i
        elif(i=="]"):
            condicion=False
            cadena+=i
        elif(condicion==True):
            cadena+=i
    return cadena

def cargar_datos_Recordatorios(ruta):
    with open(ruta, "r", encoding='utf-8') as informacion:
        info = json.load(informacion)
        for inf in info['Estudiantes']:
            print("Carnet: ", inf['Carnet'])
            age = inf['Años']
            for ag in age:
                print("Año: ", ag['Año'])
                alumnos.Alumnos_.AñadirAño(inf['Carnet'], ag['Año'], alumnos.Alumnos_.root)
                sem = ag['Semestres']
                for s in sem:
                    print("Semestre: ", s['Semestre'])
                    alumnos.Alumnos_.buscarsemestre(inf['Carnet'], ag['Año'], s['Semestre'], alumnos.Alumnos_.root)
                    cursos = s['Cursos']
                    for curso in cursos:
                        print("Codigo: ", curso['Codigo'])
                        print("Nombre: ", curso['Nombre'])
                        print("Creditos: ", str(curso['Creditos']))
                        print("Prerequisitos: ", curso['Prerequisitos'])
                        print("Obligatorio", str(curso['Obligatorio']))
                        alumnos.Alumnos_.cursosEstudiante(inf['Carnet'], ag['Año'], s['Semestre'], curso['Codigo'], curso['Nombre'], curso['Creditos'], curso['Prerequisitos'], curso['Obligatorio'], alumnos.Alumnos_.root)
                        print("")

def cargar_datos_Alumnos(ruta):
    with open(ruta, "r", encoding='utf-8') as informacion:
        info = json.load(informacion)
        for i in info['estudiantes']:
            print(i)
            print(str(i['carnet']))
            print(str(i['DPI']))
            print(i['nombre'])
            print(i['carrera'])
            print(i['correo'])
            print(i['password'])
            print(str(i['edad'])+'\n')
            ANALIZADORES_.Conex.encryp_al( str(i['carnet']), str(i['DPI']), i['nombre'], i['carrera'], i['correo'], hashlib.sha256(i['password'].encode("utf-8")).hexdigest(), str(0), str(i['edad']))

def cargar_datos_Apuntes(ruta):
    with open(ruta, "r", encoding='utf-8') as apuntes:
        apuntess = json.load(apuntes)
        for apunte in apuntess['usuarios']:
            print(apunte['carnet'])
            ap = apunte['apuntes']
            for data in ap:
                print(data['Título'])
                print(data['Contenido'])
                ANALIZADORES_.Conex.agregarinformacion(apunte['carnet'], data['Título'], data['Contenido'])