from io import open
import json

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
            print(curso.get('Codigo') + " -> " + curso.get('Nombre'))
    

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
    archivo = open(ruta, 'r', encoding='utf-8')
    texto = archivo.read()
    print(texto)