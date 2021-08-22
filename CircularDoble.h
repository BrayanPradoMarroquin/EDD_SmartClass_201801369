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
    NodoCircularDoble *actual = new NodoCircularDoble();
    actual = primero;
    string data = "";
    string pointer = "";
    int counter = 1;
    string graph = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n";
    do{
        data += "Node" + to_string(counter) + "[label=\"" + actual->Nombre +"\"];\n";
        if (actual != primero){
            pointer += "Node" + to_string(counter-1) + "->Node" + to_string(counter) + ";\n";
            pointer += "Node" + to_string(counter) + "->Node" + to_string(counter-1) + ";\n";
        }
        counter ++;
        actual = actual->siguiente;
    }while(actual != primero);
    pointer += "Node" + to_string(counter-1) + "->Node1" + ";\n";
    pointer += "Node1->Node" + to_string(counter-1) + ";\n";

    graph += data;
    graph += pointer;
    graph += "\n}";

    try {
        string path = "Student";

        ofstream file;
        file.open(path + "Graph.dot",std::ios::out);

        if(file.fail()){
            exit(1);
        }

        file<<graph;
        file.close();
        string command = "dot -Tpng " + path + "Graph.dot -o  " + path + "Graph.png";
        system(command.c_str());
    }catch (exception e){
        cout << "Nel no se pudo :)";
    }
}

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
                getline(cin>>ws, actual->carnet);
                //cin>>actual->carnet;
                cout<<"\n Ingrese el DPI: \n";
                getline(cin>>ws, actual->DPI);
                //cin>>actual->DPI;
                cout<<"\n Ingrese el Nombre: \n";
                getline(cin>>ws, actual->Nombre);
                //cin>>actual->Nombre;
                cout<<"\n Ingrese la Carrera: \n";
                getline(cin>>ws, actual->Carrera);
                //cin>>actual->Carrera;
                cout<<"\n Ingrese la Contraseña: \n";
                getline(cin>>ws, actual->Password);
                //cin>>actual->Password;
                cout<<"\n Ingrese los Creditos: \n";
                getline(cin>>ws, actual->Creditos);
                //cin>>actual->Creditos;
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
