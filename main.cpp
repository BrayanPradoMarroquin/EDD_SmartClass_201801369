#include <iostream>
#include <String>
#include <conio.h>
#include <fstream>
#include <locale.h>
#include <windows.h>
#include "Analizadores.h"
#include "Salida.h"
using namespace std;

//Area de Declaraciones Globales
string ruta_Alumno, ruta_Tareas;
ifstream Archivo_Alumno;
ifstream Archivo_Tarea;
string Entrada_Alumno, Entrada_Tarea;

//Carga de Metodos

//Ingreso Manual de los Alumnos
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
                cout<<"Carnet: "<<endl;
                cin>>carnet;
                cout<<"DPI: "<<endl;
                cin>>DPI;
                cout<<"Nombre Completo: "<<endl;
                getline(cin>>ws, Nombre);
                cout<<"Carrera: "<<endl;
                getline(cin>>ws, Carrera);
                cout<<"Correo Electronico: "<<endl;
                cin>> Correo;
                cout<<"Contrasenia: "<<endl;
                getline(cin>>ws, Contra);
                cout<<"Creditos: "<<endl;
                cin>>Creditos;
                cout<<"Edad: "<<endl;
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

//Paarseo de Meses
int ParseoMes(int mes){
    if (mes==7){ //Mes
        return 0;
    }else if(mes==8){
        return 1;
    }else if(mes==9){
        return  2;
    }else if(mes==10){
        return  3;
    }else if(mes==11){
        return 4;
    }else {
        return -1;
    }
}
//Paarseo de de dias
int Parseodia(int dia){
    if(dia>0 && dia<=30){ //dia
        return dia-1;
    }else{
        return -1;
    }
}
//Paarseo de horas
int ParseoHora(int hora){
    if (hora==8){ //Hora
        return 0;
    }else if(hora==9){
        return 1;
    }else if(hora==10){
        return 2;
    }else if(hora==11){
        return 3;
    }else if(hora==12){
        return 4;
    }else if(hora==13){
        return 5;
    }else if(hora==14){
        return 6;
    }else if(hora==15){
        return 7;
    }else if(hora==16){
        return 8;
    }else {
        return -1;
    }
}

//Ingreso Manual de las Tareas
int cargaTareas(){
    bool Menu_Usuario=true;
    int eleccion, Mes, Dia, Hora, Identificador;
    string Actividad;

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
                cout<<"Ingrese el Numero del Mes"<<endl;
                cin>>Mes;
                cout<<"Ingrese el dia: "<<endl;
                cin>>Dia;
                cout<<"Ingrese la Hora: "<<endl;
                cin>>Hora;
                Identificador = Parseodia(Dia)+30*(ParseoHora(Hora)+9*ParseoMes(Mes));
                Actividad = "NUEVO";
                TareasLinealizadas->ModificarListaDoble(Identificador, Actividad);
                break;
                case 2:
                    cout<<"Modificar Datos"<<endl;
                    cout<<"ingrese el Identificador de la Tarea: "<<endl;
                    cin>>Identificador;
                    Actividad = "MODIFICAR";
                    TareasLinealizadas->ModificarListaDoble(Identificador, Actividad);
                    break;
                    case 3:
                        cout<<"Eliminar Datos"<<endl;

                        cout<<"ingrese el Identificador de la Tarea: "<<endl;
                        cin>>Identificador;
                        Actividad = "ELIMINAR";
                        TareasLinealizadas->ModificarListaDoble(Identificador, Actividad);
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

//Menu de los Ingresos Manuales
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

//Menu de los Resportes (INACTIVO POR EL MOMENTO)
int Reportes(){
    bool Menu_Usuario=true;
    int eleccion, mes, dia, hora, identificador;
    string Actividad;

    while (Menu_Usuario==true){
        cout<<"\n************** Reportes **************"<<endl;
        cout<<"**** 1- Lista de Usuarios ************"<<endl;
        cout<<"**** 2- Linealizacion de Tareas ******"<<endl;
        cout<<"**** 3- Busqueda Linealizada *********"<<endl;
        cout<<"**** 4- Busqueda de Posicion *********"<<endl;
        cout<<"**** 5- Generar Archivo **************"<<endl;
        cout<<"**** 6- Lista de Erroes **************"<<endl;
        cout<<"**** 7- Salir ************************"<<endl;
        cout<<"Ingrese un una opcion: "; cin>>eleccion;
        switch (eleccion)
        {
            case 1:
                Menu_Usuario=false;
                Alumnos->desplegarLista();
                cout<<"Listado Generado"<<endl;
                break;
                case 2:
                    Actividad="TAREAS";
                    TareasLinealizadas->DesplegarListaDoble(Actividad);
                    cout<<"Tareas Creadas"<<endl;
                    Menu_Usuario = false;
                    break;
                    case 3:
                        cout<<"Ingrese los datos que se Solicitan"<<endl;
                        cout<<"Numero del Mes";
                        cin>>mes;
                        cout<<"Dia";
                        cin>>dia;
                        cout<<"Hora";
                        cin>>hora;
                        identificador = Parseodia(dia)+30*(ParseoHora(hora)+9*ParseoMes(mes));
                        Actividad = "TERCERO";
                        TareasLinealizadas->BuscarListaDoble(identificador, Actividad);
                        Menu_Usuario = false;
                        break;
                        case 4:
                            cout<<"Ingrese los datos que se Solicitan"<<endl;
                            cout<<"Numero del Mes: "<<endl;
                            cin>>mes;
                            cout<<"Dia: "<<endl;
                            cin>>dia;
                            cout<<"Hora: "<<endl;
                            cin>>hora;
                            identificador = Parseodia(dia)+30*(ParseoHora(hora)+9*ParseoMes(mes));
                            //identificador = ParseoMes(mes)+5*(Parseodia(dia)+30*ParseoHora(hora));
                            Actividad = "CUARTO";
                            TareasLinealizadas->BuscarListaDoble(identificador, Actividad);
                            Menu_Usuario = false;
                            break;
            case 6:
                Actividad="ERROR";
                Errores->DesplegarListaDoble(Actividad);
                break;
                            case 5:
                                if (Errores->vacio()){
                                    Alumnos->GenerarArchivo();
                                    cout<<"SE GENERO UN ARCHIVO"<<endl;
                                } else{
                                    cout<<"NO SE PUEDE GENERAR EL ARCHIVO, EXISTEN ERRORES"<<endl;
                                }
                                break;
                                case 7:
                                    Menu_Usuario = false;
                                    break;
                                    default:
                                        cout<<"Opcion no Valida"<<endl;
                                        break;
        }
    }
    return true;
}

//Entrada del Archivo de Alumnos
string Ruta_Alumnos_Abrir(string ruta){
    string text, concatenado;
    Archivo_Alumno.open(ruta.c_str(), ios::in);

    if (Archivo_Alumno.fail()){
        cout<<"Archivo no Valido, ingrese otro"<<endl;
        concatenado = "NO";
    }

    while (!Archivo_Alumno.eof()){
        getline(Archivo_Alumno, text);
        concatenado = concatenado + text + "\n";
    }
    Archivo_Alumno.close();
    return concatenado;
}

//Entrada del Archivo de Tareas
string Ruta_Tareas_Abrir(string ruta){
    string text, concatenado;
    Archivo_Tarea.open(ruta.c_str(), ios::in);

    if (Archivo_Tarea.fail()){
        cout<<"Archivo no Valido, ingrese otro"<<endl;
        concatenado = "NO";
    }

    while (!Archivo_Tarea.eof()){
        getline(Archivo_Tarea, text);
        concatenado = concatenado + text + "\n";
    }
    Archivo_Tarea.close();
    return concatenado;
}

//Menu Principal
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
                if (Entrada_Tarea!="NO"){
                    Analizador_Alumnos(Entrada_Alumno);
                }
                break;
                case 2:
                    //menu1=false;
                    cout<<"TAREAS"<<endl;
                    cout<<"Ingrese la ruta de las Tareas: "<<endl;
                    cin>>ruta_Tareas;
                    Entrada_Tarea = Ruta_Tareas_Abrir(ruta_Tareas);
                    if (Entrada_Tarea!="NO"){
                        Analizador_Tarea(Entrada_Tarea);
                        llenadomatriz();
                        Linealizar();
                    }
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
