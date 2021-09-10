import analizadores
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)


