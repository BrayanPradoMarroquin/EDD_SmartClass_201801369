//
// Created by BRAYAN on 5/08/2021.
//
#include <string>
#include <iostream>
#include "EnlazadoDoble.h"
using namespace std;

#ifndef PROYECTO_UNICO_INTENTO_2_NODOCIRCULARDOBLE_H
#define PROYECTO_UNICO_INTENTO_2_NODOCIRCULARDOBLE_H

class NodoCircularDoble{
public:
    string carnet;
    string DPI;
    string Nombre;
    string Carrera;
    string Correo;
    string Password;
    string Creditos;
    string Edad;
    EnlazadoDoble *ListaTareas = new EnlazadoDoble();
    EnlazadoDoble *tareas = ListaTareas;

    NodoCircularDoble* siguiente;
    NodoCircularDoble* atras;
};

#endif //PROYECTO_UNICO_INTENTO_2_NODOCIRCULARDOBLE_H