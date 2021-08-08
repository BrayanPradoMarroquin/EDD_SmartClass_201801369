//
// Created by BRAYAN on 5/08/2021.
//
#include <string>
#include <iostream>
using namespace std;

#ifndef PROYECTO_UNICO_INTENTO_2_NODOCIRCULARDOBLE_H
#define PROYECTO_UNICO_INTENTO_2_NODOCIRCULARDOBLE_H

class NodoCircularDoble{
public:
    int carnet;
    string DPI;
    string Nombre;
    string Carrera;
    string Correo;
    string Password;
    int Creditos;
    int Edad;

    NodoCircularDoble* siguiente;
    NodoCircularDoble* atras;
};

#endif //PROYECTO_UNICO_INTENTO_2_NODOCIRCULARDOBLE_H
