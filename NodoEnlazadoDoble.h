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
        string carnet;
        string Nombre;
        string Descripcion;
        string Fecha;
        string Hora;
        string Estado;

        NodoEnlazadoDoble* siguiente;
        NodoEnlazadoDoble* atras;
};

#endif //PROYECTO_UNICO_INTENTO_2_NODOENLAZADODOBLE_H
