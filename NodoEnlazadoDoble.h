//
// Created by BRAYAN on 6/08/2021.
//
#include <string>
#include <iostream>
using namespace std;

#ifndef PROYECTO_UNICO_INTENTO_2_NODOENLAZADODOBLE_H
#define PROYECTO_UNICO_INTENTO_2_NODOENLAZADODOBLE_H

class NodoEnlazadoDoble{
    public:
        string Id;
        string carnet;
        string Nombre;
        string Descripcion;
        string Fecha;
        string Hora;
        string Estado;

        NodoEnlazadoDoble* siguiente;
        NodoEnlazadoDoble* atras;

    public:
        NodoEnlazadoDoble();
        NodoEnlazadoDoble(string Id, string carnet, string Nombre, string Descripcion, string Fecha, string Hora, string Estado);
};

NodoEnlazadoDoble::NodoEnlazadoDoble() {
    this->Id = "";
    this->carnet ="";
    this->Nombre="";
    this->Descripcion="";
    this->Fecha="";
    this->Hora="";
    this->Estado="";
    this->siguiente=NULL;
    this->atras=NULL;
}

NodoEnlazadoDoble::NodoEnlazadoDoble(string Id, string carnet, string Nombre, string Descripcion, string Fecha,
                                     string Hora, string Estado) {
    this->Id = Id;
    this->carnet =carnet;
    this->Nombre=Nombre;
    this->Descripcion=Descripcion;
    this->Fecha=Fecha;
    this->Hora=Hora;
    this->Estado=Estado;

    this->siguiente=NULL;
    this->atras=NULL;
}

#endif //PROYECTO_UNICO_INTENTO_2_NODOENLAZADODOBLE_H
