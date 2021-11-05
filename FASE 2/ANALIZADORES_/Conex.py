from ESTRUCTURAS_.NodoArbolAVL import NodoArbolAVL_
import alumnos
from cryptography.fernet import Fernet
from ESTRUCTURAS_.TablaHash import NodoCont
from ESTRUCTURAS_.Grafo import Arista
from ESTRUCTURAS_.Grafo import Grafo

file = open('key.key', 'rb')
key = file.read()
file.close()
keygen = Fernet(key)

def encryp_al(carnet, DPI, nombre, carrera, correo, password, creditos, edad):
    
    estudiante = NodoArbolAVL_(carnet, keygen.encrypt(carnet.encode()), keygen.encrypt(DPI.encode()), keygen.encrypt(nombre.encode()), keygen.encrypt(carrera.encode()), keygen.encrypt(correo.encode()), keygen.encrypt(password.encode()), keygen.encrypt(creditos.encode()), keygen.encrypt(edad.encode()))
    alumnos.Alumnos_.insert(estudiante)

def decryp_al(carnet):
    return alumnos.Alumnos_.Buscar_evento(alumnos.Alumnos_.root, carnet)
    
def encryp_ac_al(carnet, DPI, nombre, carrera, correo, password, creditos, edad):
    alumnos.Alumnos_.Mod_Estudiante(carnet, keygen.encrypt(DPI.encode()), keygen.encrypt(nombre.encode()), keygen.encrypt(carrera.encode()), keygen.encrypt(correo.encode()), keygen.encrypt(password.encode()), keygen.encrypt(creditos.encode()), keygen.encrypt(edad.encode()), alumnos.Alumnos_.root)

def agregarinformacion(carnet, titulo, descripcion):
    alumnos.Apuntes.agregar(NodoCont(carnet))
    alumnos.Apuntes.cargarInf(carnet, titulo, descripcion)

def buscar(codigo):
    alumnos.Cursos = Grafo()
    da = buscarmalla(codigo)
    alumnos.Cursos.graficar()

def buscarmalla(codigo):
    datos = alumnos.Pensum.buscar(codigo)
    if (datos!=""):
        alumnos.Cursos.agregar(Arista(datos[0], datos[1], datos[2], datos[3]))
        for pre in datos[3]:
            if(pre!=''):
                da = buscarmalla(pre)
            else:
                pass
    return 