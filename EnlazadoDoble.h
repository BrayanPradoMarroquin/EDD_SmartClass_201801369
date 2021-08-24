//
// Created by BRAYAN on 6/08/2021.
//
#include <iostream>
#include <iostream>
using namespace std;
#include "NodoEnlazadoDoble.h"

#ifndef PROYECTO_UNICO_INTENTO_2_ENLAZADODOBLE_H
#define PROYECTO_UNICO_INTENTO_2_ENLAZADODOBLE_H

class EnlazadoDoble{
private:
    NodoEnlazadoDoble* primero;
    NodoEnlazadoDoble* ultimo;

public:
    void InsertarNodoDoble(string&, string&, string&, string&, string&, string&, int&);
    void DesplegarListaDoble(string&);
    void BuscarListaDoble(int&, string&);
    void ModificarListaDoble(int&, string&);
    bool vacio();
    EnlazadoDoble();

    string Retorno();
};

EnlazadoDoble::EnlazadoDoble(){
    this->primero = NULL;
    this->ultimo = NULL;
}

bool EnlazadoDoble::vacio(){
    if(primero==NULL){
        return true;
    } else{
        return false;
    }
}

//METODO INTERNO DE INGRESO DE DATOS
void EnlazadoDoble::InsertarNodoDoble(string& carnet, string& nombre, string& descripcion, string& fecha, string& hora, string& estado, int& ID){
    NodoEnlazadoDoble* nuevo = new NodoEnlazadoDoble();
    nuevo->Id = ID;
    nuevo->carnet = carnet;
    nuevo->Nombre = nombre;
    nuevo->Descripcion = descripcion;
    nuevo->Fecha = fecha;
    nuevo->Materia = hora;
    nuevo->Estado = estado;

    if (primero==NULL){
        primero = nuevo;
        primero->siguiente = NULL;
        primero->atras = NULL;
        ultimo = primero;
    }else{
        ultimo->siguiente = nuevo;
        nuevo->siguiente = NULL;
        nuevo->atras = ultimo;
        ultimo = nuevo;
    }
}

//GENERADOR DE REPORTE GENERAL
void EnlazadoDoble::DesplegarListaDoble(string& Actividad){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    string data = "", path = "";
    string pointer = "";
    int counter = 1;
    string graph = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n";
    do {
        if (Actividad=="TAREAS"){
            path = "Tareas";
            if(actual->carnet=="-1"){
                cout << "Identificador: " << actual->Id << "\\nDescripcion: " << actual->carnet << '\n';
            }else{
                data += "Node"+ to_string(counter) + "[label=\" Id: " + to_string(actual->Id) + "\\n Carnet:" + actual->carnet + "\\n Materia: " + actual->Materia + "\\n Nombre: "+ actual->Nombre + "\\n Descripcion: " + actual->Descripcion + "\\n Estado: " + actual->Estado + "\\n Fecha: " + actual->Fecha + "\"];\n";
                if (actual->atras != NULL){
                    pointer += "Node" + to_string(counter-1) + "->Node" + to_string(counter) + ";\n";
                    pointer += "Node" + to_string(counter) + "->Node" + to_string(counter-1) + ";\n";
                }
                counter++;
            }
        }else if(Actividad=="ERROR"){
            path = "Errores";
            if (actual->carnet==" - 2"){
                cout << "Identificador: " << actual->Id << "\\nDescripcion: " << actual->carnet << '\n';
            }else{
                data += "Node"+ to_string(counter) + "[label=\" Id: " + to_string(actual->Id) + "\\n Tipo de Error:" + actual->Nombre + "\\n Descripcion: " + actual->Descripcion + "\\n Concepto: "+ actual->carnet + "\"];\n";
                if (actual->atras != NULL){
                    pointer += "Node" + to_string(counter-1) + "->Node" + to_string(counter) + ";\n";
                    pointer += "Node" + to_string(counter) + "->Node" + to_string(counter-1) + ";\n";
                }
                counter++;
            }
        }
        actual = actual->siguiente;
    }while (actual != NULL);
    graph += data;
    graph += pointer;
    graph += "\n}";

    try {

        ofstream file;
        file.open(path + "Reporte.dot",std::ios::out);

        if(file.fail()){
            exit(1);
        }

        file<<graph;
        file.close();
        string command = "dot -Tpng " + path + "Reporte.dot -o  " + path + "Reporte.png";
        system(command.c_str());
    }catch (exception e){
        cout << "Error detectado, no se pudo generar el Reporte solicitado";
    }
}

//GENERADOR DE REPORTES
void EnlazadoDoble::BuscarListaDoble(int& identificador, string& Reporte){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    bool encontrado = false;
    if (primero!=NULL){
        while (actual!=NULL){
            if(actual->Id==identificador){
                if(Reporte=="TERCERO"){
                    cout<<"Identificador de la tarea: "<<actual->Id<<endl;
                }else if(Reporte=="CUARTO"){
                    cout<<"Identificador: "<<actual->Id<<endl;
                    cout<<"Estudiante: "<<actual->carnet<<endl;
                    cout<<"Nombre: "<<actual->Nombre<<endl;
                    cout<<"Descripcion: "<<actual->Descripcion<<endl;
                    cout<<"Estado de ejecucion: "<<actual->Estado<<endl;
                    encontrado = true;
                }
            }
            actual = actual->siguiente;
        }
        if (!encontrado){
            cout<<"Tarea no encontrada \n";
        }
    }else{
        cout<<"LA LISTA SE ENCUENTRA VACIA"<<endl;
    }
    delete actual;
}

//ACCION MULTIPLES {INGRESAR, MODIFICAR, ELIMINAR}
void EnlazadoDoble::ModificarListaDoble(int & Identificador, string& Actividad){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    bool encontrado = false;
    if (actual!=NULL  && encontrado!=true){
        while (actual!=NULL){
            if(actual->Id==Identificador){
                if(Actividad=="NUEVO"){
                    cout<<"Ingrese el Carnet: "<<endl;
                    getline(cin>>ws, actual->carnet);
                    cout<<"Ingrese el Nombre de la Tarea: "<<endl;
                    getline(cin>>ws, actual->Nombre);
                    cout<<"Ingrese la Descripcion de la Tarea: "<<endl;
                    getline(cin>>ws, actual->Descripcion);
                    cout<<"Ingrese la Fecha de Entrega: "<<endl;
                    cin>>actual->Fecha;
                    cout<<"Ingrese la Materia: "<<endl;
                    getline(cin>>ws, actual->Materia);
                    cout<<"Ingrese el Estado: "<<endl;
                    cin>>actual->Estado;
                } else if (Actividad=="MODIFICAR"){
                    cout<<"Carnet: "<<endl;
                    getline(cin>>ws, actual->carnet);
                    cout<<"Nombre de la Tarea: "<<endl;
                    getline(cin>>ws, actual->Nombre);
                    cout<<"Descripcion de la Tarea: "<<endl;
                    getline(cin>>ws, actual->Descripcion);
                    cout<<"Fecha de Entrega: "<<endl;
                    cin>>actual->Fecha;
                    cout<<"Materia: "<<endl;
                    //cin>>actual->Materia;
                    getline(cin>>ws, actual->Materia);
                    cout<<"Estado: "<<endl;
                    cin>>actual->Estado;
                }else if (Actividad=="ELIMINAR"){
                    actual->carnet = "-1";
                    actual->Nombre = "-1";
                    actual->Descripcion = "-1";
                    actual->Fecha = "-1";
                    actual->Materia = "-1";
                    actual->Estado = "-1";
                }
                encontrado = true;
            }

            actual = actual->siguiente;
        }
        if (!encontrado){
            cout<<"nodo no encontrado \n";
        }
    }else{
        cout<<"LA LISTA SE ENCUENTRA VACIA"<<endl;
    }
}


//Retorno de Tareas
string EnlazadoDoble::Retorno(){
    NodoEnlazadoDoble *task = new NodoEnlazadoDoble();
    task = primero;
    string data = "";
    do {
        data += "¿element type=\"task\"? \n";
        data += "¿item Carnet  =\"" + task->carnet + "\" $? \n";
        data += "¿item Nombre  =\"" + task->Nombre + "\" $? \n";
        data += "¿item Descripcion  =\"" + task->Descripcion + "\" $? \n";
        data += "¿item Materia  =\"" + task->Materia + "\" $? \n";
        data += "¿item Fecha  =\"" + task->Fecha + "\" $? \n";
        data += "¿item Estado  =\"" + task->Estado + "\" $? \n";
        data += "¿$ element? \n";

        task = task->siguiente;
    } while (task!=NULL);
    return data;
}
#endif //PROYECTO_UNICO_INTENTO_2_ENLAZADODOBLE_H