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
    bool BuscarListaDoble(string&);
    void ModificarListaDoble(string &);
    void EliminarListaDoble(string&);
    EnlazadoDoble();
};

EnlazadoDoble::EnlazadoDoble(){
    this->primero = NULL;
    this->ultimo = NULL;
}

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

bool EnlazadoDoble::BuscarListaDoble(string & carnet){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    bool encontrado = false;
    if (primero!=NULL){
        while (actual!=NULL){
            if(actual->carnet==carnet){
                cout<<"Nodo encontrado :"<<actual->carnet<<endl;
                return true;
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

void EnlazadoDoble::ModificarListaDoble(string& carnet){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    bool encontrado = false;
    if (actual!=NULL  && encontrado!=true){
        while (actual!=NULL){
            if(actual->carnet==carnet){
                cin>>actual->carnet;
                cout<<"Dato actualizado \n";
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

void EnlazadoDoble::EliminarListaDoble(string & carnet){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    NodoEnlazadoDoble* anterior = new NodoEnlazadoDoble();
    NodoEnlazadoDoble* borrador = new NodoEnlazadoDoble();
    anterior = NULL;
    bool encontrado = false;
    if (primero!=NULL){
        while (actual!=NULL  && encontrado!=true){
            if(actual->carnet==carnet){
                cout<<actual->carnet<<endl;
                if (actual==primero){
                    borrador = actual;
                    primero = primero->siguiente;
                    primero->atras = NULL;
                    delete borrador;
                }else if (actual==ultimo){
                    borrador = actual;
                    anterior->siguiente = NULL;
                    ultimo = anterior;
                    delete borrador;
                }else{
                    borrador = actual;
                    anterior->siguiente = actual->siguiente;
                    actual->siguiente->atras = anterior;
                    delete borrador;
                }
                cout<<"Dato eliminado \n";
                encontrado = true;
            }
            anterior = actual;
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
