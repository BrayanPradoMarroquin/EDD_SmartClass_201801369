import ANALIZADORES_.analizadores
from flask import Flask, request, jsonify
from flask_cors import CORS
import ANALIZADORES_.analizadoralumnos
import ANALIZADORES_.Conex 
from NodoTask import Tareas
import alumnos

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hola Mundo"

##----------------------------- Area de Alumnos -------------------------------

@app.route("/estudiante", methods=['POST', 'PUT'])
def IngresoEstudiante():
    if request.method == 'POST':
        obten = request.json
        ANALIZADORES_.Conex.encryp_al( obten['carnet'], obten['DPI'], obten['Nombre'], obten['Carrera'], obten['Correo'], obten['Contraseña'], obten['Creditos'], obten['Edad'])
        data = {
            'respuesta': "El usuario: " + obten['carnet'] +" se ha ingresado con Exito"
        }
        return data
    elif request.method == 'PUT':
        carnet = request.args.get('carnet', 'no contiene este parametro')
        DPI = request.args.get('DPI', 'no contiene este parametro')
        nombre = request.args.get('nombre', 'no contiene este parametro')
        carrera = request.args.get('carrera', 'no contiene este parametro')
        correo = request.args.get('correo', 'no contiene este parametro')
        password = request.args.get('password', 'no contiene este parametro')
        creditos = request.args.get('creditos', 'no contiene este parametro')
        edad = request.args.get('edad', 'no contiene este parametro')
        ANALIZADORES_.Conex.encryp_ac_al(carnet, DPI, nombre, carrera, correo, password, creditos, edad)
        return "Los Datos han sido actualizados"

@app.route("/Apunte", methods=['POST'])
def IngresarApunte():
    obten = request.json
    ANALIZADORES_.Conex.agregarinformacion(obten['usuario'], obten['titulo'], obten['contenido'])
    return obten

##---------------------------- Area General --------------------------------------

@app.route("/carga", methods=['POST'])
def Carga():
    obten = request.json
    tipo = obten['tipo']
    ruta = obten['ruta'].split('\\')
    if(tipo=="estudiante"):
        ANALIZADORES_.analizadores.cargar_datos_Alumnos(ruta[2])
        print("vamo a ver si lleno los años")
        return "Estudiantes" + " -> " + ruta[2]
    elif(tipo=="recordatorio"):
        ANALIZADORES_.analizadores.cargar_datos_Recordatorios(ruta[2])
        return "Recordatorio" + " -> " + ruta[2]
    elif(tipo=="curso"):
        ANALIZADORES_.analizadores.cargar_datos_Pensum(ruta[2])
        return "datos llenados correctamente"

@app.route("/reporte", methods=['POST'])
def Reporte():
    obten = request.json
    tipo = obten['tipo']
    if(tipo=="0"):
        alumnos.Alumnos_.graficar("encriptado", alumnos.Alumnos_.root)
        alumnos.Alumnos_.graficar("decriptado", alumnos.Alumnos_.root)
        data = {
            'respuesta': "Reporte Alumno Generado"
        }
        return data
    elif(tipo=="1"):
        alumnos.Apuntes.graficar()
        data = {
            'respuesta': "Reporte de Apuntes Generado"
        }
        return data
    elif(tipo=="2"):
        hor = obten['hora'].split(":")
        alumnos.Alumnos_.graphTareas(obten['carnet'], obten['año'], obten['mes'], obten['dia'], int(hor[0]), alumnos.Alumnos_.root)
        return "Reporte Tareas Generado"
    elif(tipo=="3"):
        #alumnos.Pensum.Preorden()
        return "Reporte de Cursos del Pensum Generado"
    elif(tipo=="4"):
        return "Reporte de Cursos del semestre"

@app.route("/Login", methods=['POST'])
def Login():
    obten = request.json
    return alumnos.Alumnos_.Buscar_evento(alumnos.Alumnos_.root, obten['usuario'], obten['password'])
    

if __name__ == '__main__':
    app.run(debug=True, port=3000)

##-----------------------Realizado Por: Brayan Hamllelo Estevem Prado Marroquin - 201801369

