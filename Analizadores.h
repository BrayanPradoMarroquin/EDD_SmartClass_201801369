//
// Created by BRAYAN on 6/08/2021.
//
#include <iostream>
#include <string>
#include "CircularDoble.h"
#include "NodoEnlazadoDoble.h"
#include "EnlazadoDoble.h"
using namespace std;

#ifndef PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
#define PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H
ListaCircularDoble *Alumnos = new ListaCircularDoble();
EnlazadoDoble *TareasLinealizadas = new EnlazadoDoble();
EnlazadoDoble *Errores = new EnlazadoDoble();

string Cont = "", Tipo="", Descripcion="", vacio="";
int Estado=0, EstadoTarea=0, EstadoTareaAuxiliar=0;
int contador = 0, ContadorErrores = 0; //activa el contador
string Datos[8], DatoTarea[9];
NodoEnlazadoDoble* Matriz[5][30][9];


//ANALIZADOR DE ALUMNOS
void Analisis_Alumno(char &i);

int Analisis_Tarea(char &i, int& conta);

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
                Tipo="Alumno";
                Descripcion = "carnet no valido";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
                Estado = 0;
                Cont = "";
            }
        }else if(Assci==44 && contador==9){
            Datos[0] = Cont;
            contador = 0;
            Cont = "";
            Estado=2;
        } else{
            Tipo="Alumno";
            Descripcion = "carnet no valido";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
            Estado = 0;
            Cont = "";
        }
    }else if(Estado==2){ // para el DPI
        int Assci = caracter; //pasar a Ascci
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=13){ //concatena y aumenta 1
                Cont = Cont + caracter;
            }else{
                Tipo="Alumno";
                Descripcion = "DPI no valido";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
                Estado = 0;
                Cont = "";
                contador = 0;
            }
        }else if(Assci==44 && contador==13){
            Datos[1] = Cont;
            Cont = "";
            contador = 0;
            Estado=3;
        }else{
            Tipo="Alumno";
            Descripcion = "DPI no valido";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado==3){ //NOMBRE DEL ISHTO
        int Assci = caracter; //pasar a Ascci
        if ((Assci>=97 && Assci<=122) || (Assci>=65 && Assci<=90) || (Assci==32)){ //Letras y espacios
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[2] = Cont;
            Cont = "";
            contador = 0;
            Estado=4;
        }else{
            Tipo="Alumno";
            Descripcion = "Nombre no valido";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado == 4){ //Carrera del patojo
        int Assci = caracter; //pasar a Ascci
        if ((Assci>=97 && Assci<=122) || (Assci>=65 && Assci<=90) || (Assci==32)){ //Letras y espacios
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[3] = Cont;
            Cont = "";
            contador = 0;
            Estado=5;
        }else{
            Tipo="Alumno";
            Descripcion = "la Carrera contiene simbolos anormales";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
            Estado = 0;
            Cont = "";
            contador = 0;
        }
    }else if(Estado==5){ //Contraseña
        int Assci = caracter; //pasar a Ascci
        if(Assci==44){
            Datos[4] = Cont;
            Cont = "";
            contador = 0;
            Estado=6;
        }else{
            Cont = Cont + caracter;
        }
    }else if(Estado==6){ //Creditos
        int Assci = caracter; //pasar a Ascci
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            Cont = Cont + caracter;
        }else if(Assci==44){
            Datos[5] = Cont;
            Cont = "";
            contador = 0;
            Estado=7;
        }else{
            Tipo="Alumno";
            Descripcion = "Los creditos solo aceptan solo digitos";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
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
            Tipo="Alumno";
            Descripcion = "Las edades solo aceptan solo digitos";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
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
            Alumnos->insertarNodo(Datos[0], Datos[1], Datos[2], Datos[3], Datos[4], Datos[5],Datos[6], Datos[7]);
        }else{
            Cont = Cont + caracter;
        }
    }
}

//ANALIZADOR DE LAS TAREAS
void Analizador_Tarea(string entrada){
    int contadorID = 0;
    for (int i=0; i<entrada.size(); i++){
        int Assci = entrada[i];
        if(Assci == 10 && EstadoTarea==0){
            EstadoTarea = 1;
        }else if(EstadoTarea>0){
            contadorID = Analisis_Tarea(entrada[i], contadorID);
        }
    }

}
//MES, DIA, HORA
int Analisis_Tarea(char &caracter, int& contadorID) {
    int Assci = caracter;
    if(EstadoTarea==1){ //MES
        if (Assci>=48 && Assci<=57){ //0-9
            Cont += caracter;
        } else if(Assci==44){
            EstadoTarea = 2;
            DatoTarea[0] = Cont;
            Cont = "";
        }else{
            Tipo="Tarea";
            Descripcion = "Los meses no son en letras -> [7-11]";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);

        }
    } else if (EstadoTarea==2){ //DIA
        if (Assci>=48 && Assci<=57){ //0,1,2,3
            Cont +=caracter;
        }else if(Assci==44){
            EstadoTarea = 3;
            DatoTarea[1] = Cont;
            Cont = "";
        }else{
            Tipo="Tarea";
            Descripcion = "Los dias no son en letras -> [1-30]";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
        }
    } else if (EstadoTarea==3){ //HORAS
        if (Assci>=48 && Assci<=57){ //0,1
            Cont +=caracter;
        }else if(Assci==44){
            EstadoTarea = 4;
            DatoTarea[2] = Cont;
            Cont = "";
        }else{
            Tipo="Tarea";
            Descripcion = "Las horas no son en letras -> [8-16]";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
        }
    } else if(EstadoTarea==4){ //CARNET'S
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=9){ //concatena y aumenta 1
                Cont = Cont + caracter;
            }else{
                Tipo="Tarea";
                Descripcion = "El carnet no es valido";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
                EstadoTarea = 0;
                Cont = "";
            }
        }else if(Assci==44 && contador==9){
            DatoTarea[3] = Cont;
            contador = 0;
            Cont = "";
            EstadoTarea=5;
        }else{
            Tipo="Tarea";
            Descripcion = "Los meses no son en letras -> [7-11]";
            ContadorErrores++;
            Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
            EstadoTarea = 0;
            Cont = "";
        }
    } else if(EstadoTarea==5){ //nombre
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
            int Posm,Posh,Posd;
            string Descripcion;
            DatoTarea[8]=Cont;
            Cont="";
            contador=0;
            EstadoTarea = 1;

            if (DatoTarea[0]=="7"){ //Mes
                Posm=0;
            }else if(DatoTarea[0]=="8"){
                Posm=1;
            }else if(DatoTarea[0]=="9"){
                Posm=2;
            }else if(DatoTarea[0]=="10"){
                Posm=3;
            }else if(DatoTarea[0]=="11"){
                Posm=4;
            }else {
                Posm=-1;
                Descripcion = "Se encontro un error en el mes ingresado [fuera de rango]";
            }

            if (DatoTarea[2]=="8"){ //Hora
                Posh=0;
            }else if(DatoTarea[2]=="9"){
                Posh=1;
            }else if(DatoTarea[2]=="10"){
                Posh=2;
            }else if(DatoTarea[2]=="11"){
                Posh=3;
            }else if(DatoTarea[2]=="12"){
                Posh=4;
            }else if(DatoTarea[2]=="13"){
                Posh=5;
            }else if(DatoTarea[2]=="14"){
                Posh=6;
            }else if(DatoTarea[2]=="15"){
                Posh=7;
            }else if(DatoTarea[2]=="16"){
                Posh=8;
            }else {
                Posh=-1;
                Descripcion = "Se encontro un error en la hora ingresado [fuera de rango]";
            }

            if(atoi(DatoTarea[1].c_str())>0 && atoi(DatoTarea[1].c_str())<=30){ //dia
                Posd=1;
            }else{
                Posd=-1;
                Descripcion = "Se encontro un error en el dia ingresado [fuera de rango]";
            }

            cout<<Posm<<" - "<<atoi(DatoTarea[1].c_str())-1<<" - "<<Posh<<endl;
            if (Posm==-1 || Posh==-1 || Posd==-1){
                //ListaErrores.insert();
                cout<<"ERRORES";
                Tipo="Tarea";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
            }else{
                //cout<<DatoTarea[3]<<" "<<DatoTarea[4]<<DatoTarea[5]<<" "<<DatoTarea[6]<<endl;
                cout<<DatoTarea[7];
                NodoEnlazadoDoble *aux = new NodoEnlazadoDoble();
                aux->Id = contadorID++;
                aux->carnet = DatoTarea[3];
                aux->Nombre = DatoTarea[4];
                aux->Descripcion = DatoTarea[5];
                aux->Materia = DatoTarea[6];
                aux->Fecha = DatoTarea[7];
                aux->Estado = DatoTarea[8];
                //remplazar el NULL por el auxiliar
                Matriz[Posm][atoi(DatoTarea[1].c_str())-1][Posh] = aux;
            }
        }
    }
}

void llenadomatriz(){

    NodoEnlazadoDoble *aux = new NodoEnlazadoDoble();
    aux->carnet = "-1";
    for (int i=0; i<5; i++){
        for (int j = 0; j < 30; ++j) {
            for (int k = 0; k < 9; ++k) {
                if (Matriz[i][j][k]==NULL){
                    Matriz[i][j][k] = aux;
                }
            }
        }
    }
}

void Linealizar(){

    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 30; ++j) {
            for (int k = 0; k < 9; ++k) {
                int Id;
                Id= i+5*(j+30*k);
                TareasLinealizadas->InsertarNodoDoble(Matriz[i][j][k]->carnet, Matriz[i][j][k]->Nombre, Matriz[i][j][k]->Descripcion, Matriz[i][j][k]->Fecha, Matriz[i][j][k]->Materia, Matriz[i][j][k]->Estado,
                                                      Id);
                //cout<<"Tarea Ingresada"<<endl;
            }
        }
    }
    cout<<"LINEALIZACION COMPLETADA"<<endl;
    //TareasLinealizadas->DesplegarListaDoble();
}

char Fechador(char &caracter){ // YYYY/MM/DD
    int Assci = caracter;
    if(EstadoTareaAuxiliar==0){ // AÑOS/
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=4){ //concatena y aumenta 1
                return caracter;
            }else{
                Tipo="Tarea";
                Descripcion = "Los años son 4 digitos, revise";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
                Estado = 0;
                Cont = "";
            }
        } else if(Assci==47 && contador==4){
            EstadoTareaAuxiliar=1;
            return caracter;
        }
    } else if(EstadoTareaAuxiliar==1){ // MESES/
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=2){ //concatena y aumenta 1
                return caracter;
            }else{
                Tipo="Tarea";
                Descripcion = "Los meses son 2 digitos, revise";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
                Estado = 0;
                Cont = "";
            }
        } else if(Assci==47 && contador==2){
            EstadoTareaAuxiliar=2;
            return caracter;
        }
    } else if(EstadoTareaAuxiliar==2){
        if (Assci >= 48 && Assci<=57){ //validar si es un numero
            contador++; //suma 1 al contador
            if (contador<=2){ //concatena y aumenta 1
                return caracter;
            }else{
                Tipo="Tarea";
                Descripcion = "Los dias son 2 digitos, revise";
                ContadorErrores++;
                Errores->InsertarNodoDoble(vacio, Tipo, Descripcion, vacio, vacio,vacio, ContadorErrores);
                Estado = 0;
                Cont = "";
            }
        }
    }
}
#endif //PROYECTO_UNICO_INTENTO_2_ANALIZADORES_H