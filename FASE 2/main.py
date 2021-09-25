import ANALIZADORES_.analizadores
from flask import Flask, request, jsonify
from ESTRUCTURAS_.NodoArbolAVL import NodoArbolAVL_
import alumnos
import ANALIZADORES_.analizadoralumnos
from NodoTask import Tareas

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"

##----------------------------- Area de Alumnos -------------------------------

@app.route("/estudiante", methods=['POST'])
def IngresoEstudiante():
    carnet = request.args.get('carnet', 'no contiene este parametro')
    DPI = request.args.get('DPI', 'no contiene este parametro')
    nombre = request.args.get('nombre', 'no contiene este parametro')
    carrera = request.args.get('carrera', 'no contiene este parametro')
    correo = request.args.get('correo', 'no contiene este parametro')
    password = request.args.get('password', 'no contiene este parametro')
    creditos = request.args.get('creditos', 'no contiene este parametro')
    edad = request.args.get('edad', 'no contiene este parametro')
    estudiante = NodoArbolAVL_(carnet, DPI, nombre, carrera, correo, password, creditos, edad)
    alumnos.Alumnos_.insert(estudiante)
    return "Nuevo estudiante"

@app.route("/estudiante", methods=['PUT'])
def ActEstudiante():
    carnet = request.args.get('carnet', 'no contiene este parametro')
    DPI = request.args.get('DPI', 'no contiene este parametro')
    nombre = request.args.get('nombre', 'no contiene este parametro')
    carrera = request.args.get('carrera', 'no contiene este parametro')
    correo = request.args.get('correo', 'no contiene este parametro')
    password = request.args.get('password', 'no contiene este parametro')
    creditos = request.args.get('creditos', 'no contiene este parametro')
    edad = request.args.get('edad', 'no contiene este parametro')
    alumnos.Alumnos_.Mod_Estudiante(carnet, DPI, nombre, carrera, correo, password, creditos, edad, alumnos.Alumnos_.root)
    return "Los Datos han sido actualizados"

@app.route("/estudiante", methods=['GET'])
def EnvEstudiante():
    carnet = request.args.get('carnet', 'no contiene este parametro')
    datos = alumnos.Alumnos_.Buscar_evento(alumnos.Alumnos_.root, carnet)
    return jsonify(datos)

##----------------------------- Area de Tareas ----------------------------------

@app.route("/recordatorios", methods=['POST'])
def CreTarea():
    carnet = request.args.get('Carnet', 'no contiene este parametro')
    fech = request.args.get('Fecha', 'no contiene este parametro')
    Fecha = fech.split("/")
    Hora = request.args.get('Hora', 'no contiene este parametro')
    nombre = request.args.get('Nombre', 'no contiene este parametro')
    descripcion = request.args.get('Descripcion', 'no contiene este parametro')
    materia = request.args.get('Materia', 'no contiene este parametro')
    status = request.args.get('Estado', 'no contiene este parametro')
    NewTask = Tareas(carnet, nombre, descripcion, materia, fech, Hora, status)
    NewTask.direccionamiento = Fecha
    datos = alumnos.Alumnos_.newAll(NewTask, alumnos.Alumnos_.root)
    return "La tarea ha sido actualizada"

@app.route("/recordatorios", methods=['GET'])
def EnvTarea():
    carnet = request.args.get('Carnet', 'no contiene este parametro')
    Fecha = request.args.get('Fecha', 'no contiene este parametro').split("/")
    Hora = request.args.get('Hora', 'no contiene este parametro')
    Id = request.args.get('Identificador', 'no contiene este parametro')
    datos = alumnos.Alumnos_.RecuTarea(carnet, Fecha[2], Fecha[1], Fecha[0], Hora,Id, alumnos.Alumnos_.root)
    return jsonify(datos)

@app.route("/recordatorios", methods=['PUT'])
def ActTarea():
    carnet = request.args.get('Carnet', 'no contiene este parametro')
    fech = request.args.get('Fecha', 'no contiene este parametro')
    Fecha = fech.split("/")
    Hora = request.args.get('Hora', 'no contiene este parametro')
    Id = request.args.get('Identificador', 'no contiene este parametro')
    nombre = request.args.get('Nombre', 'no contiene este parametro')
    descripcion = request.args.get('Descripcion', 'no contiene este parametro')
    materia = request.args.get('Materia', 'no contiene este parametro')
    status = request.args.get('Estado', 'no contiene este parametro')
    datos = alumnos.Alumnos_.actualizarTarea(carnet, Fecha[2], Fecha[1], Fecha[0], Hora,Id, nombre, descripcion, materia, fech, status, alumnos.Alumnos_.root)
    return "La tarea ha sido actualizada"

##---------------------------- Area General --------------------------------------

@app.route("/carga", methods=['POST'])
def Carga():
    tipo = request.args.get('tipo', 'no contiene este parametro')
    ruta = request.args.get('ruta', 'no contiene este parametro')
    if(tipo=="estudiante"):
        ANALIZADORES_.analizadoralumnos.alumno(ruta)
        ANALIZADORES_.analizadoralumnos.sintac()
        ANALIZADORES_.analizadoralumnos.sintacT()
        print("vamo a ver si lleno los años")
        return "Estudiantes" + " -> " + ruta
    elif(tipo=="recordatorio"):
        ANALIZADORES_.analizadores.cargar_datos_Recordatorios(ruta)
        return "Recordatorio" + " -> " + ruta
    elif(tipo=="curso"):
        ANALIZADORES_.analizadores.cargar_datos_Pensum(ruta)
        return "datos llenados correctamente"

@app.route("/reporte", methods=['POST'])
def Reporte():
    obten = request.json
    tipo = obten['tipo']
    if(tipo=="0"):
        alumnos.Alumnos_.preShow(alumnos.Alumnos_.root)
        alumnos.Alumnos_.graficar(alumnos.Alumnos_.root)
        return "Reporte Alumno Generado"
    elif(tipo=="1"):
        return "Reporte Matriz Generado"
    elif(tipo=="2"):
        alumnos.Alumnos_.graphTareas(obten['carnet'], obten['año'], obten['mes'], obten['dia'], obten['hora'], alumnos.Alumnos_.root)
        return "Reporte Tareas Generado"
    elif(tipo=="3"):
        alumnos.Pensum.Preorden()
        return "Reporte de Cursos del Pensum Generado"
    elif(tipo=="4"):
        return "Reporte de Cursos del semestre"

@app.route("/buscar", methods=['POST'])
def Buscar():
    data = request.args.get('data', 'no contiene este parametro')
    resultado = alumnos.Alumnos_.Buscar_evento(alumnos.Alumnos_.root, data)
    return resultado

if __name__ == '__main__':
    app.run(debug=True, port=3000)

##-----------------------Realizado Por: Brayan Hamllelo Estevem Prado Marroquin - 201801369

