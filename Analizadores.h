//
// Created by BRAYAN on 6/08/2021.
//
#include <iostream>
#include <string>
#include "CircularDoble.h"
#include "NodoEnlazadoDoble.h"
using namespace std;

#ifndef PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
#define PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
ListaCircularDoble Alumnos;
string Cont = "";
int Estado=0, EstadoTarea=0, EstadoTareaAuxiliar=0;
int contador = 0; //activa el contador
string Datos[8];
NodoEnlazadoDoble* Matriz[5][30][8];
string DatoTarea[9];

//ANALIZADOR DE ALUMNOS
void Analisis_Alumno(char &i);

void Analisis_Tarea(char &i);

char Fechador(char &i);

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
            Alumnos.insertarNodo(Datos[0], Datos[1], Datos[2], Datos[3], Datos[4], Datos[5],Datos[6], Datos[7]);
        }else{
            Cont = Cont + caracter;
        }
    }
}

//ANALIZADOR DE LAS TAREAS
void Analizador_Tarea(string entrada){
    for (int i=0; i<entrada.size(); i++){
        int Assci = entrada[i];
        if(Assci == 10 && EstadoTarea==0){
            Estado = 1;
        }else if(Estado>0){
            Analisis_Tarea(entrada[i]);
        }
    }
}
//MES, DIA, HORA
void Analisis_Tarea(char &caracter) {
    int Assci = caracter;
    if(EstadoTarea==1){ //MES
        if (Assci>=55 && Assci<=57){ //7,8,9
            Cont = caracter;
            EstadoTarea = 2;
        }else if(Assci==49){ //1
            Cont +=caracter;
            EstadoTarea = 1;
        } else if(Assci>=48 && Assci<=49){ //0, 1
            Cont +=caracter;
        } else if(Assci==44){
            EstadoTarea = 2;
            DatoTarea[0] = Cont;
            Cont = "";
        }
    } else if (EstadoTarea==2){ //DIA
        if (Assci>=48 && Assci<=51){ //0,1,2,3
            Cont +=caracter;
        } else if(Assci>=48 && Assci<=57){
            Cont += caracter;
        }else if(Assci==44){
            EstadoTarea = 3;
            DatoTarea[1] = Cont;
            Cont = "";
        }
    } else if (EstadoTarea==3){ //HORAS
        if (Assci>=48 && Assci<=49){ //0,1
            Cont +=caracter;
        } else if((Assci>=48 && Assci<=52) && (Assci>=56 && Assci<=57)){ //0{48},1{49},2{50},3{51},4{52} - 8,9
            Cont += caracter;
        }else if(Assci==44){
            EstadoTarea = 4;
            DatoTarea[2] = Cont;
            Cont = "";
        }
    } else if(EstadoTarea==4){ //CARNET'S
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=9){ //concatena y aumenta 1
                Cont = Cont + caracter;
            }else{
                EstadoTarea = 0;
                Cont = "";
            }
        }else if(Assci==44){
            DatoTarea[3] = Cont;
            contador = 0;
            Cont = "";
            EstadoTarea=5;
        }
    } else if(EstadoTarea==5){ //nombre, descripcion, materia
        if(Assci==44){
            DatoTarea[4] = Cont;
            Cont = "";
            contador = 0;
            EstadoTarea=6;
        }else{
            Cont += caracter;
        }
    } else if(EstadoTarea==6){//Descripcion
        if(Assci==44){
            DatoTarea[5] = Cont;
            Cont = "";
            contador = 0;
            EstadoTarea=7;
        }else{
            Cont += caracter;
        }
    }else if(EstadoTarea==7){ //Materia
        if(Assci==44){
            DatoTarea[6] = Cont;
            Cont = "";
            contador = 0;
            EstadoTarea=8;
        }else{
            Cont += caracter;
        }
    }else if(EstadoTarea==8){//Fecha
        if (Assci==44){
            EstadoTareaAuxiliar=0;
            DatoTarea[7] = Cont;
            Cont = "";
            contador = 0;
            EstadoTarea=9;
        } else{
            Cont = Cont + Fechador(caracter);
        }
    } else if(EstadoTarea==9){
        if((Assci>=65 && Assci<=90) && (Assci>=97 && Assci<=122)){
            Cont +=caracter;
        } else if(Assci==10){
            int Posh, Posm;
            DatoTarea[8]=Cont;
            Cont="";
            contador=0;
            EstadoTarea = 1;
            if (DatoTarea[0]=="7"){
                Posm=0;
            } else if(DatoTarea[0]=="8"){
                Posm=1;
            }
            if (DatoTarea[2]=="8"){
                Posh=0;
            } else if(DatoTarea[2]=="9"){
                Posh=1;
            }
            Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh]->carnet = DatoTarea[3];
            Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh]->Nombre = DatoTarea[4];
            Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh]->Descripcion = DatoTarea[5];
            Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh]->Hora = DatoTarea[6];
            Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh]->Fecha = DatoTarea[7];
            Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh]->Estado = DatoTarea[8];
        }
    }
}

char Fechador(char &caracter){ // YYYY/MM/DD
    int Assci = caracter;
    if(EstadoTareaAuxiliar==0){ // AÑOS/
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=4){ //concatena y aumenta 1
                return caracter;
            }else{
                Estado = 0;
                Cont = "";
            }
        } else if(Assci==47){
            EstadoTareaAuxiliar=1;
            return caracter;
        }
    } else if(EstadoTareaAuxiliar==1){ // MESES/
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=2){ //concatena y aumenta 1
                return caracter;
            }else{
                Estado = 0;
                Cont = "";
            }
        } else if(Assci==47){
            EstadoTareaAuxiliar=2;
            return caracter;
        }
    } else if(EstadoTareaAuxiliar==2){
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=2){ //concatena y aumenta 1
                return caracter;
            }else{
                Estado = 0;
                Cont = "";
            }
        }
    }
}
#endif //PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
