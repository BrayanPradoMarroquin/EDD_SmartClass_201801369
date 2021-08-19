//
// Created by BRAYAN on 6/08/2021.
//
#include <iostream>
#include <String>
#include "NodoCircularDoble.h"
using namespace std;

#ifndef PROYECTO_CIRCULARDOBLE_H
#define PROYECTO_CIRCULARDOBLE_H

class ListaCircularDoble{
private:
    NodoCircularDoble* primero;
    NodoCircularDoble* ultimo;
public:
    void insertarNodo(string& carnet, string& DPI, string& Nombre, string& Carrera, string& Contra, string& Creditos, string& Edad, string& Correo);
    void desplegarLista();
    bool buscarNodo(string& carnet);
    void modificarNodo(string& carnet);
    void EliminarNodo(string&);
    void GraficarLista();
    ListaCircularDoble();
};
ListaCircularDoble::ListaCircularDoble() {
    this->primero = NULL;
    this->ultimo = NULL;
}

void ListaCircularDoble::insertarNodo(string& carnet, string& DPI, string& Nombre, string& Carrera, string& Contra, string& Creditos, string& Edad, string& Correo){
    NodoCircularDoble* nuevo = new NodoCircularDoble();
    nuevo->carnet = carnet;
    nuevo->DPI = DPI;
    nuevo->Nombre = Nombre;
    nuevo->Carrera = Carrera;
    nuevo->Password = Contra;
    nuevo->Creditos = Creditos;
    nuevo->Edad = Edad;
    nuevo->Correo = Correo;

    cout<<nuevo->carnet;

    if (primero==NULL){
        primero = nuevo;
        ultimo = nuevo;
        primero->siguiente = primero;
        primero->atras = ultimo;
    }else{
        ultimo->siguiente = nuevo;
        nuevo->atras = ultimo;
        nuevo->siguiente = primero;
        ultimo = nuevo;
        primero->atras = ultimo;
    }
    cout<<"\n Nodo Ingresado \n";
}

void ListaCircularDoble::desplegarLista(){

}

/*void ListaCircularDoble::desplegarLista(){
    NodoCircularDoble* actual = new NodoCircularDoble();
    actual = primero;
    FILE *Archivo;
    Archivo = fopen("grafo.dot","w+");
    fprintf(Archivo, "digraph G { \\n");
    string cont ="";
    string rec = "";
    if(primero!=NULL){
        do{
            if(actual==primero){
                cont = cont +actual->carnet+"[label=\""+"Carnet: "+ actual->carnet+"\\n Nombre: "+ actual->Nombre+" \\n DPI: "+actual->DPI+"\\n";
                cont = cont +" Carrera: "+ actual->Carrera+"\\n Password: "+actual->Password+"\\n Creditos: "+actual->Creditos+"\\n Edad: "+actual->Edad+" \\n Correo: "+actual->Correo+"\"] \\n";
                actual = actual->siguiente;
            }else if(actual!=primero && actual!=ultimo){
                cont = cont +actual->carnet+"[label=\""+"Carnet: "+ actual->carnet+"\\n Nombre: "+ actual->Nombre+" \\n DPI: "+actual->DPI+"\\n";
                cont = cont +" Carrera: "+ actual->Carrera+"\\n Password: "+actual->Password+"\\n Creditos: "+actual->Creditos+"\\n Edad: "+actual->Edad+" \\n Correo: "+actual->Correo+"\"] \\n";
                rec = actual->atras->carnet+"<->"+actual->carnet;
                actual = actual->siguiente;
            }else if(actual==ultimo){
                cont = cont +actual->carnet+"[label=\""+"Carnet: "+ actual->carnet+"\\n Nombre: "+ actual->Nombre+" \\n DPI: "+actual->DPI+"\\n";
                cont = cont +" Carrera: "+ actual->Carrera+"\\n Password: "+actual->Password+"\\n Creditos: "+actual->Creditos+"\\n Edad: "+actual->Edad+" \\n Correo: "+actual->Correo+"\"] \\n";
                rec = actual->carnet+"<->"+actual->siguiente->carnet;
                actual = actual->siguiente;
            }
            fprintf(Archivo, cont);
            if(rec!=""){
                fprintf(Archivo, rec);
                rec="";
            }
        }while(actual!=primero);
        fprintf(Archivo,"}");
        fclose(Archivo);
        system("dot grafo.dot -o Reporte_Alumno.jpg -Tjpg -Grankdir=TB && xdg-open Reporte_Alumno.jpg");
    }else{
        cout<<"\n La lista se Encuentra Vacia \n";

    }
}
*/
bool ListaCircularDoble::buscarNodo(string& carnet){
    NodoCircularDoble* actual = new NodoCircularDoble();
    actual = primero;
    bool encontrado = false;
    if(primero!=NULL){
        do{
            if(actual->carnet==carnet){
                //cout<<"\n Nodo con el dato: "<<carnet<<" Encontrado\n";
                return true;
            }
            actual = actual->siguiente;
        }while(actual!=primero && encontrado!= true);
        if (!encontrado){
            cout<<"\n Nodo no encontrado \n";
        }
    }else{
        cout<<"\n La lista se Encuentra Vacia \n";

    }
}

void ListaCircularDoble::modificarNodo(string& carnet){
    NodoCircularDoble* actual = new NodoCircularDoble();
    actual = primero;
    bool encontrado = false;
    if(primero!=NULL){
        do{
            if(actual->DPI==carnet){
                cout<<"\n Nodo con el dato: "<<carnet<<" Encontrado\n";
                cout<<"\n Ingrese el carnet: \n";
                cin>>actual->carnet;
                cout<<"\n Ingrese el DPI: \n";
                cin>>actual->DPI;
                cout<<"\n Ingrese el Nombre: \n";
                cin>>actual->Nombre;
                cout<<"\n Ingrese la Carrera: \n";
                cin>>actual->Carrera;
                cout<<"\n Ingrese la Contraseña: \n";
                cin>>actual->Password;
                cout<<"\n Ingrese los Creditos: \n";
                cin>>actual->Creditos;
                cout<<"\n Ingrese la Edad: \n";
                cin>>actual->Edad;
                cout<<"\n Ingrese el Correo electronico: \n";
                cin>>actual->Correo;
                cout<<"\n nodo Modificado";
                encontrado=true;
            }
            actual = actual->siguiente;
        }while(actual!=primero && encontrado!= true);
        if (!encontrado){
            cout<<"\n Nodo no encontrado \n";
        }
    }else{
        cout<<"\n La lista se Encuentra Vacia \n";

    }
}

void ListaCircularDoble::EliminarNodo(string& carnet){
    NodoCircularDoble* actual = new NodoCircularDoble();
    actual = primero;
    NodoCircularDoble* anterior = new NodoCircularDoble();
    anterior = NULL;
    bool encontrado = false;
    if(primero!=NULL){
        do{
            if(actual->DPI==carnet){
                cout<<"\n Nodo con el dato: "<<carnet<<" Encontrado\n";
                if (actual==primero){
                    primero = primero->siguiente;
                    primero->atras=ultimo;
                    ultimo->siguiente = primero;
                }else if(actual==ultimo){
                    ultimo = anterior;
                    ultimo->siguiente = primero;
                    primero->atras = ultimo;
                }else{
                    anterior->siguiente = actual->siguiente;
                    actual->siguiente->atras = anterior;
                }
                cout<<"\n Nodo Eliminado \n";
                encontrado=true;
            }
            anterior = actual;
            actual = actual->siguiente;
        }while(actual!=primero && encontrado!= true);
        if (!encontrado){
            cout<<"\n Nodo no encontrado \n";
        }
    }else{
        cout<<"\n La lista se Encuentra Vacia \n";

    }
}


#endif //PROYECTO_CIRCULARDOBLE_H
