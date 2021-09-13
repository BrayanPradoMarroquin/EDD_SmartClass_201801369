import analizadores
from flask import Flask, request
from NodoArbolAVL import NodoArbolAVL_
import alumnos

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"

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

@app.route("/carga", methods=['POST'])
def Carga():
    tipo = request.args.get('tipo', 'no contiene este parametro')
    ruta = request.args.get('ruta', 'no contiene este parametro')
    if(tipo=="estudiante"):

        return "Estudiantes" + " -> " + ruta
    elif(tipo=="recordatorio"):
        analizadores.cargar_datos_Recordatorios(ruta)
        return "Recordatorio" + " -> " + ruta
    elif(tipo=="curso"):
        analizadores.cargar_datos_Pensum(ruta)
        return "datos llenados correctamente"

@app.route("/reporte", methods=['POST'])
def Reporte():
    tipo = request.args.get('tipo', 'no contiene este parametro')
    if(tipo=="0"):
        alumnos.Alumnos_.preShow(alumnos.Alumnos_.root)
        alumnos.Alumnos_.graficar(alumnos.Alumnos_.root)
        return "Reporte Alumno Generado"

@app.route("/buscar", methods=['POST'])
def Buscar():
    data = request.args.get('data', 'no contiene este parametro')
    resultado = alumnos.Alumnos_.Buscar_evento(alumnos.Alumnos_.root, data)
    return resultado

if __name__ == '__main__':
    app.run(debug=True, port=3000)


