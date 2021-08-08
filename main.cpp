#include <iostream>
#include <String>
#include <conio.h>
#include <fstream>
#include <locale.h>
#include <windows.h>
#include "CircularDoble.h"
#include "Analizadores.h"
using namespace std;

//Area de Declaraciones Globales
string ruta_Alumno;
string ruta_Tareas;
ifstream Archivo_Alumno;
ifstream Archivo_Tarea;
string Entrada_Alumno;
string Entrada_Tarea;

//Carga de Metodos
int cargaUsuario(){
    bool Menu_Usuario=true;
    int eleccion;
    int carnet, Creditos, Edad;
    string Nombre, Carrera, Correo, Contra, DPI;

    while (Menu_Usuario==true){
        cout<<"\n************** Usuario **************"<<endl;
        cout<<"**** 1- Ingresar ********************"<<endl;
        cout<<"**** 2- Modificar *******************"<<endl;
        cout<<"**** 3- Eliminar ********************"<<endl;
        cout<<"**** 4- Salir ***********************"<<endl;
        cout<<"Ingrese un una opcion: "; cin>>eleccion;
        switch (eleccion){
            case 1:
                Menu_Usuario=false;
                cout<<"Ingresar Datos"<<endl;
                cout<<"Ingrese los datos que contendra el nuevo Nodo: \n";
                cin>>carnet;
                cin>>DPI;
                cin>>Nombre;
                cin>>Carrera;
                cin>>Correo;
                cin>>Contra;
                cin>>Creditos;
                cin>>Edad;
                Alumnos.insertarNodo(carnet, DPI, Nombre, Carrera, Contra, Creditos, Edad, Correo);
                break;
                case 2:
                    cout<<"Modificar Datos"<<endl;
                    break;
                    case 3:
                        cout<<"Eliminar Datos"<<endl;
                        break;
                        case 4:
                            Menu_Usuario = false;
                            break;
                            default:
                                cout<<"Opcion no Valida"<<endl;
                                break;
        }
    }
    return true;
}

int cargaTareas(){
    bool Menu_Usuario=true;
    int eleccion;

    while (Menu_Usuario==true){
        cout<<"\n************** Tareas ***************"<<endl;
        cout<<"**** 1- Ingresar ********************"<<endl;
        cout<<"**** 2- Modificar *******************"<<endl;
        cout<<"**** 3- Eliminar ********************"<<endl;
        cout<<"**** 4- Salir ***********************"<<endl;
        cout<<"Ingrese un una opcion: "; cin>>eleccion;
        switch (eleccion)
        {
            case 1:
                Menu_Usuario=false;
                cout<<"Ingresar Datos"<<endl;
                break;
                case 2:
                    cout<<"Modificar Datos"<<endl;
                    break;
                    case 3:
                        cout<<"Eliminar Datos"<<endl;
                        break;
                        case 4:
                            Menu_Usuario = false;
                            break;
                            default:
                                cout<<"Opcion no Valida"<<endl;
                                break;
        }

    }
    return true;
}

int Manual(){
    bool Menu_Usuario=true;
    int eleccion;

    while (Menu_Usuario==true){
        cout<<"\n************** MENU **************"<<endl;
        cout<<"**** 1- Usuarios ********************"<<endl;
        cout<<"**** 2- Tareas **********************"<<endl;
        cout<<"**** 3- Salir ***********************"<<endl;
        cout<<"Ingrese un una opcion: "; cin>>eleccion;
        switch (eleccion)
        {
            case 1:
                Menu_Usuario=false;
                Menu_Usuario = cargaUsuario();
                break;
                case 2:
                    Menu_Usuario=false;
                    Menu_Usuario = cargaTareas();
                    break;
                    case 3:
                        Menu_Usuario = false;
                        break;
                        default:
                            cout<<"Opcion no Valida"<<endl;
                            break;
        }
    }
    return true;
}

int Reportes(){
    bool Menu_Usuario=true;
    int eleccion;

    while (Menu_Usuario==true){
        cout<<"\n************** Reportes **************"<<endl;
        cout<<"**** 1- Lista de Usuarios ************"<<endl;
        cout<<"**** 2- Linealizacion de Tareas ******"<<endl;
        cout<<"**** 3- Salir ************************"<<endl;
        cout<<"Ingrese un una opcion: "; cin>>eleccion;
        switch (eleccion)
        {
            case 1:
                //Menu_Usuario=false;
                cout<<"Listado Generado"<<endl;
                break;
                case 2:
                    cout<<"Tareas Creadas"<<endl;
                    break;
                    case 3:
                        Menu_Usuario = false;
                        break;
                        default:
                            cout<<"Opcion no Valida"<<endl;
                            break;
        }
    }
    return true;
}

string Ruta_Alumnos_Abrir(string ruta){
    string text, concatenado;
    Archivo_Alumno.open(ruta.c_str(), ios::in);

    if (Archivo_Alumno.fail()){
        cout<<"Archivo no Valido, ingrese otro"<<endl;
        Ruta_Alumnos_Abrir(ruta);
    }

    while (!Archivo_Alumno.eof()){
        getline(Archivo_Alumno, text);
        concatenado = concatenado + text + "\n";
    }
    return concatenado;
}

int main(){
    bool menu1=true;
    int eleccion;

    while (menu1==true)
    {
        cout<<"\n********* MENU - SMART CLASS ***************"<<endl;
        cout<<"*** 1. Carga de Usuarios *******************"<<endl;
        cout<<"*** 2. Carga de Tareas *********************"<<endl;
        cout<<"*** 3. Ingreso Manual **********************"<<endl;
        cout<<"*** 4. Reportes ****************************"<<endl;
        cout<<"*** 5. Salir *******************************"<<endl;
        cout<<"********************************************"<<endl;

        cout<<"Ingrese un una opcion: "; cin>>eleccion;
        switch (eleccion)
        {
            case 1:
                //menu1=false
                cout<<"USUARIOS"<<endl;
                cout<<"Ingrese la ruta de los Alumnos: "<<endl;
                cin>>ruta_Alumno;
                Entrada_Alumno = Ruta_Alumnos_Abrir(ruta_Alumno);
                Analizador_Alumnos(Entrada_Alumno);
                break;
                case 2:
                    //menu1=false;
                    cout<<"TAREAS"<<endl;
                    break;
                    case 3:
                        menu1=false;
                        menu1 = Manual();
                        break;
                        case 4:
                            menu1=false;
                            menu1 = Reportes();
                            break;
                            case 5:
                                cout<<"Salir"<<endl;
                                menu1=false;
                                break;
                                default:
                                    cout<<"Opcion no Valida"<<endl;
                                    break;
        }
    }
    return 0;
}
