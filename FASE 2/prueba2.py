from io import open
import json

def cargar_datos_Recordatorios():
    with open("CursosEstudiante.json", "r", encoding='utf-8') as informacion:
        info = json.load(informacion)
        for inf in info['Estudiantes']:
            print("Carnet: ", inf['Carnet'])
            age = inf['Años']
            for ag in age:
                print("Año: ", ag['Año'])
                sem = ag['Semestres']
                for s in sem:
                    print("Semestre: ", s['Semestre'])
                    cursos = s['Cursos']
                    for curso in cursos:
                        print("Codigo: ", curso['Codigo'])
                        print("Nombre: ", curso['Nombre'])
                        print("Creditos: ", str(curso['Creditos']))
                        print("Prerequisitos: ", curso['Prerequisitos'])
                        print("Obligatorio", str(curso['Obligatorio']))
                        print("")

cargar_datos_Recordatorios()