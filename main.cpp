#include <iostream>
#include <String>
#include <conio.h>
#include <fstream>
#include <locale.h>
#include <windows.h>
#include "Analizadores.h"
using namespace std;

//Area de Declaraciones Globales
string ruta_Alumno, ruta_Tareas;
ifstream Archivo_Alumno;
ifstream Archivo_Tarea;
string Entrada_Alumno, Entrada_Tarea;

//Carga de Metodos
int cargaUsuario(){
    bool Menu_Usuario=true;
    int eleccion;
    string Nombre, Carrera, Correo, Contra, DPI, carnet, Creditos, Edad, eliminacion;

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
                Alumnos->insertarNodo(carnet, DPI, Nombre, Carrera, Contra, Creditos, Edad, Correo);
                break;
                case 2:
                    cout<<"Modificar Datos"<<endl;
                    cout<<"Ingrese en DPI del alumno: "<<endl;
                    cin>>carnet;
                    Alumnos->modificarNodo(carnet);
                    break;
                    case 3:
                        cout<<"Eliminar Datos"<<endl;
                        cout<<"Ingrese en DPI del alumno: "<<endl;
                        cin>>carnet;
                        cout<<"¿Esta seguro que desea eliminar el dato con carnet: "<<carnet<<", elija SI o NO"<<endl;
                        cin>>eliminacion;
                        if(eliminacion=="SI"){
                            Alumnos->EliminarNodo(carnet);
                        }else if(eliminacion=="NO"){
                            cout<<"\n El dato no a sido eliminado "<<endl;
                        }
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
                Alumnos->desplegarLista();
                cout<<"Listado Generado"<<endl;
                break;
                case 2:
                    TareasLinealizadas->DesplegarListaDoble();
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
    }

    while (!Archivo_Alumno.eof()){
        getline(Archivo_Alumno, text);
        concatenado = concatenado + text + "\n";
    }
    Archivo_Alumno.close();
    return concatenado;
}

string Ruta_Tareas_Abrir(string ruta){
    string text, concatenado;
    Archivo_Tarea.open(ruta.c_str(), ios::in);

    if (Archivo_Tarea.fail()){
        cout<<"Archivo no Valido, ingrese otro"<<endl;
        return "ERROR";
    }

    while (!Archivo_Tarea.eof()){
        getline(Archivo_Tarea, text);
        concatenado = concatenado + text + "\n";
    }
    Archivo_Tarea.close();
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
                    cout<<"Ingrese la ruta de las Tareas: "<<endl;
                    cin>>ruta_Tareas;
                    Entrada_Tarea = Ruta_Tareas_Abrir(ruta_Tareas);
                    if (Entrada_Tarea!="ERROR"){
                    	Analizador_Tarea(Entrada_Tarea);	
                    }
                    llenadomatriz();
                    Linealizar();
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
