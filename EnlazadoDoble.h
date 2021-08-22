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
    void DesplegarListaDoble();
    void BuscarListaDoble(int&, string&);
    void ModificarListaDoble(int&, string&);
    EnlazadoDoble();
};

EnlazadoDoble::EnlazadoDoble(){
    this->primero = NULL;
    this->ultimo = NULL;
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
void EnlazadoDoble::DesplegarListaDoble(){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    if (primero!=NULL){
        while (actual!=NULL){
            cout<<actual->Id<<" --> "<<actual->carnet<<" la Tarea es: "<<actual->Nombre<<" y descripcion: "<<actual->Descripcion<<endl;
            cout<<actual->Fecha<<" del curso: "<<actual->Materia<<" y el estado es: "<<actual->Estado<<endl;
            actual = actual->siguiente;
        }
    }else{
        cout<<"LA LISTA SE ENCUENTRA VACIA"<<endl;
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
                cout<<"Tarea encontrada con Id:"<<actual->Id<<endl<<endl;
                if(Reporte=="TERCERO"){
                    string grafico = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n";
                    string datos = "Node"+(string&) actual->Id + "[label=\"Identificador: " + (string&) actual->Id + "\\n Nombre: "+actual->Nombre+"\\n Descripcion: "+actual->Descripcion+"\\n Estado de ejecucion: "+actual->Estado+"\"];\n";
                    grafico += datos;
                    grafico +="\n}";
                    try {
                        ofstream file;
                        file.open("Consulta.dot",std::ios::out);

                        if(file.fail()){
                            exit(1);
                        }

                        file<<grafico;
                        file.close();
                        string command = "dot -Tpng  Consulta.dot -o  Consulta.png";
                        system(command.c_str());
                        cout<<"Se genero la Tarea"<<endl;
                        encontrado = true;
                    }catch (exception e){
                        cout << "Nel no se pudo :)";
                    }

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

#endif //PROYECTO_UNICO_INTENTO_2_ENLAZADODOBLE_H
