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
    void InsertarNodoDoble(int&, string&, string&, string&, string&, string&);
    void DesplegarListaDoble();
    void BuscarListaDoble(int&);
    void ModificarListaDoble(int&);
    void EliminarListaDoble(int&);
};

void EnlazadoDoble::InsertarNodoDoble(int& carnet, string& nombre, string& descripcion, string& fecha, string& hora, string& estado){
    NodoEnlazadoDoble* nuevo = new NodoEnlazadoDoble();
    nuevo->carnet = carnet;
    nuevo->Nombre = nombre;
    nuevo->Descripcion = descripcion;
    nuevo->Fecha = fecha;
    nuevo->Hora = hora;
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
            cout<<actual->carnet<<" la Tarea es: "<<actual->Nombre<<" y descripcion: "<<actual->Descripcion<<endl;
            cout<<actual->Fecha<<" a las. "<<actual->Hora<<" y el estado es: "<<actual->Estado<<endl;
            actual = actual->siguiente;
        }
    }else{
        cout<<"LA LISTA SE ENCUENTRA VACIA"<<endl;
    }
}

void EnlazadoDoble::BuscarListaDoble(int& carnet){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    bool encontrado = false;
    if (primero!=NULL){
        while (actual!=NULL){
            if(actual->carnet==carnet){
                cout<<"Nodo encontrado :"<<actual->carnet<<endl;
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

void EnlazadoDoble::ModificarListaDoble(int& carnet){
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

void EnlazadoDoble::EliminarListaDoble(int& carnet){
    NodoEnlazadoDoble* actual = new NodoEnlazadoDoble();
    actual = primero;
    nodo* anterior = new nodo();
    anterior = NULL;
    bool encontrado = false;
    if (primero!=NULL){
        while (actual!=NULL  && encontrado!=true){
            if(actual->carnet==carnet){
                cout<<actual->carnet<<endl;
                if (actual==primero){
                    primero = primero->siguiente;
                    primero->atras = NULL;
                }else if (actual==ultimo){
                    anterior->siguiente = NULL;
                    ultimo = anterior;
                }else{
                    anterior->siguiente = actual->siguiente;
                    actual->siguiente->atras = anterior;
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
