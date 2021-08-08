//
// Created by BRAYAN on 6/08/2021.
//
#include <iostream>
#include <string>
#include "CircularDoble.h"
using namespace std;

#ifndef PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
#define PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
ListaCircularDoble Alumnos;
string Cont = "";
int Estado=0;
int contador = 0; //activa el contador - CAMBIAR
string Datos[8];
//ANALIZADOR DE ALUMNOS
void Analisis_Alumno(char &i);

void Analizador_Alumnos(string entrada){
    for (int i=0; i<entrada.size(); i++){
        int Assci = entrada[i];
        if(Assci == 10 && Estado==0){
            Estado = 1;
        }else if(Estado>0){
            Analisis_Alumno(entrada[i]);
        }
    }
}

void Analisis_Alumno(char &caracter) {
    if(Estado==1){ //Carnet's
        int Assci = caracter; //pasar a Ascci
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
                if (contador<=9){ //concatena y aumenta 1
                    Cont = Cont + caracter;
                }else{
                    Estado = 0;
                    Cont = "";
                }
        }else if(Assci==44){
            Datos[0] = Cont;
            contador = 0;
            Cont = "";
            Estado=2;
        }
    }else if(Estado==2){ // para el DPI
        int Assci = caracter; //pasar a Ascci
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=13){ //concatena y aumenta 1
                Cont = Cont + caracter;
            }else{
                Estado = 0;
                Cont = "";
                contador = 0;
            }
        }else if(Assci==44){
            Datos[1] = Cont;
            Cont = "";
            contador = 0;
            Estado=3;
        }else{
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado==3){
        int Assci = caracter; //pasar a Ascci
        if ((Assci>=97 && Assci<=122) || (Assci>=65 && Assci<=90) || (Assci==32)){ //Letras y espacios
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[2] = Cont;
            Cont = "";
            contador = 0;
            Estado=4;
        }else{
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado == 4){
        int Assci = caracter; //pasar a Ascci
        if ((Assci>=97 && Assci<=122) || (Assci>=65 && Assci<=90) || (Assci==32)){ //Letras y espacios
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[3] = Cont;
            Cont = "";
            contador = 0;
            Estado=5;
        }else{
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado==5){
        int Assci = caracter; //pasar a Ascci
        if(Assci==44){
            Datos[4] = Cont;
            Cont = "";
            contador = 0;
            Estado=6;
        }else{
            Cont = Cont + caracter;
        }
    }else if(Estado==6){
        int Assci = caracter; //pasar a Ascci
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[5] = Cont;
            Cont = "";
            contador = 0;
            Estado=7;
        }else{
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado==7){ //para las edades
        int Assci = caracter; //pasar a Ascci
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[6] = Cont;
            Cont = "";
            contador = 0;
            Estado=8;
        }else{
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado==8){
        int Asscci = caracter;
        if (Asscci==10){
            Datos[7] = Cont;
            Cont = "";
            contador = 0;
            Estado=1;
            Alumnos.insertarNodo(reinterpret_cast<int &>(Datos[0]), Datos[1], Datos[2], Datos[3], Datos[4], reinterpret_cast<int &>(Datos[5]),
                                 reinterpret_cast<int &>(Datos[6]), Datos[7]);
        }else{
            Cont = Cont + caracter;
        }
    }
}

//ANALIZADOR DE LAS TAREAS
#endif //PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
