from ESTRUCTURAS_.ARBOLB_.PaginaB import PaginaB
import os

class BTree:
    def __init__(self):
        self.Raiz=PaginaB()
        self.Codigo=0
        self.Pais= ""
        self.creditos = ""
        self.Prerequisitos = ""
        self.Obligatorio = False

        self.auxiliar1=False
        self.Auxliar2=PaginaB()
        self.subeArriba=False
        self.estado=False
        self.comparador=False
        
        self.grafica=""
        self.grafica2=PaginaB()
        self.pais=""
        self.nodos=0
    
    def estaVacio(self, raiz):
        return ((raiz==None) | (raiz.getCuenta()==0))
    
    def InsertarDatos(self, codigo, pais, creditos, Prerequisitos, Obligatorio):
        self.InsertarDatos2(self.Raiz,codigo, pais, creditos, Prerequisitos, Obligatorio)
    
    def InsertarDatos2(self, raiz, codigo, pais, creditos, Prerequisitos, Obligatorio):
        self.Empujar(raiz,codigo, pais, creditos, Prerequisitos, Obligatorio)
        if(self.subeArriba):
            self.Raiz= PaginaB()
            self.Raiz.setCuenta(1)
            self.Raiz.setCodigo(0, self.Codigo)
            self.Raiz.setPais(0, self.Pais)
            self.Raiz.setCreditos(0, self.creditos)
            self.Raiz.setPrerequisitos(0, self.Prerequisitos)
            self.Raiz.setObligatorio(0, self.Obligatorio)

            self.Raiz.setApuntador(0, raiz)
            self.Raiz.setApuntador(1, self.Auxliar2)
    
    def Empujar(self, raiz, codigo, pais, creditos, Prerequisitos, Obligatorio):
        posicion = 0
        self.estado=False
        
        if(self.estaVacio(raiz) & self.comparador==False):
            self.subeArriba=True
            
            self.Codigo=codigo
            self.Pais=pais
            self.creditos = creditos
            self.Prerequisitos = Prerequisitos
            self.Obligatorio = Obligatorio
            
            self.Auxliar2=None
        else :
            posicion=self.BuscarNodoB(codigo,raiz)
            if(self.comparador==False):
                if(self.estado):
                    self.subeArriba=False
                else:
                    self.Empujar(raiz.getApuntador(posicion),codigo, pais, creditos, Prerequisitos, Obligatorio)
                    if(self.subeArriba):
                        if(raiz.getCuenta()<4):
                            self.subeArriba=False
                            self.MeterHoja(raiz,posicion,self.Codigo,self.Pais, self.creditos, self.Prerequisitos, self.Obligatorio)
                        else:
                            self.subeArriba=True
                            self.DividirPaginaB(raiz,posicion,self.Codigo,self.Pais, self.creditos, self.Prerequisitos, self.Obligatorio)
            else :
                print("Dato repetido"+ codigo)
                self.comparador=False
    
    def BuscarNodoB(self, codigo, raiz):
        auxContador=0

        if(codigo.compareTo(raiz.getCodigo(0))<0):
            self.estado=False
            
            auxContador=0
        else:
            while(auxContador!=raiz.getCuenta()):
                if(codigo==raiz.getCodigo(auxContador)):
                    self.comparador=True
                auxContador+=1
            auxContador=raiz.getCuenta()
            
            while(codigo.compareTo(raiz.getCodigo(auxContador-1))<0 & auxContador>1):
                auxContador-=1
                
                if(codigo==raiz.getCodigo(auxContador-1)):
                    self.estado = True
                else:
                    self.estado=False

        return auxContador
    
    def MeterHoja(self, raiz, posicion, codigo, pais, creditos, Prerequisitos, Obligatorio):
        auxC=raiz.getCuenta()
        
        while(auxC!=posicion):
            if(auxC!=0):
                raiz.setCodigo(auxC, raiz.getCodigo(auxC-1))
                raiz.setPais(auxC, raiz.getPais(auxC-1))
                raiz.setCreditos(auxC, raiz.getCreditos(auxC-1))
                raiz.setPrerequisitos(auxC, raiz.getPrerequisitos(auxC-1))
                raiz.setObligatorio(auxC, raiz.getObligatorio(auxC-1))
                raiz.setApuntador(auxC+1, raiz.getApuntador(auxC))
            auxC-=1
        
        raiz.setCodigo(posicion, codigo)
        raiz.setPais(posicion, pais)
        raiz.setCreditos(posicion, creditos)
        raiz.setPrerequisitos(posicion, Prerequisitos)
        raiz.setObligatorio(posicion, Obligatorio)

        raiz.setApuntador(posicion+1, this.Auxliar2)
        raiz.setCuenta(raiz.getCuenta()+1)
    
    def DividirPaginaB(self, raiz, posicion, codigo, pais, creditos, Prerequisitos, Obligatorio):
        posicion2=0
        posicionMedia=0
        
        if(posicion<=2):
            posicionMedia=2
        else:
            posicionMedia=3
        
        paginaDerecha= PaginaB()
        posicion2=posicionMedia+1
        
        while(posicion2!=5):
            
            if((posicion2-posicionMedia)!=0):
                paginaDerecha.setCodigo((posicion2-posicionMedia)-1, raiz.getCodigo(posicion2-1))
                paginaDerecha.setPais((posicion2-posicionMedia)-1, raiz.getPais(posicion2-1))
                paginaDerecha.setCreditos((posicion2-posicionMedia)-1, raiz.getCreditos(posicion2-1))
                paginaDerecha.setPrerequisitos((posicion2-posicionMedia)-1, raiz.getPrerequisitos(posicion2-1))
                paginaDerecha.setObligatorio((posicion2-posicionMedia)-1, raiz.getObligatorio(posicion2-1))
                paginaDerecha.setApuntador(posicion2-posicionMedia, raiz.getApuntador(posicion2))
            posicion2+=1
        
        paginaDerecha.setCuenta(4-posicionMedia)
        raiz.setCuenta(posicionMedia)
        
        if(posicion<=2):
            self.auxiliar1=True
            self.MeterHoja(raiz,posicion,codigo, pais, creditos, Prerequisitos, Obligatorio)
        else:
            self.auxiliar1=True
            self.MeterHoja(paginaDerecha,(posicion-posicionMedia),codigo, pais, creditos, Prerequisitos, Obligatorio)
        
        self.Codigo=raiz.getCodigo(raiz.getCuenta()-1)
        self.Pais=raiz.getPais(raiz.getCuenta()-1)
        self.creditos=raiz.getCreditos(raiz.getCuenta()-1)
        self.Prerequisitos=raiz.getPrerequisitos(raiz.getCuenta()-1)
        self.Obligatorio=raiz.getObligatorio(raiz.getCuenta()-1)

        paginaDerecha.setApuntador(0, raiz.getApuntador(raiz.getCuenta()))
        
        raiz.setCuenta(raiz.getCuenta()-1)
        self.Auxliar2=paginaDerecha
        
        if(self.auxiliar1):
            raiz.setCodigo(3, "")
            raiz.setPais(3, "")
            raiz.setCreditos(3, "")
            raiz.setPrerequisitos(3, "")
            raiz.setObligatorio(3, "")
            raiz.setApuntador(4, None)
            
            raiz.setCodigo(2, "")
            raiz.setPais(2, "")
            raiz.setCreditos(2, "")
            raiz.setPrerequisitos(2, "")
            raiz.setObligatorio(2, "")
            raiz.setApuntador(3, None)
    
    def  Preorden(self):
        self.Preorden2(self.Raiz)
    
    def Preorden2(self, pagina):
        if(pagina!=None):
            
            for i in range(pagina.getCuenta()):
                if(pagina.getCodigo(i)!=None):
                    if(pagina.getCodigo(i)!=""):
                        print("Codigo: "+str(pagina.getCodigo(i))+" \nCurso: "+pagina.getPais(i)+" \nCreditos: "+str(pagina.getCreditos(i))+" \nPrerequisitos: "+pagina.getPrerequisitos(i)+" \nObligatorio "+str(pagina.getObligatorio(i)))
            print("")
            
            self.Preorden2(pagina.getApuntador(0))
            self.Preorden2(pagina.getApuntador(1))
            self.Preorden2(pagina.getApuntador(2))
            self.Preorden2(pagina.getApuntador(3))
            self.Preorden2(pagina.getApuntador(4))
    
    def Graficar(self, tipo):
        file = open("BTree.dot", 'w')

        self.grafica="digraph ArbolB{\n"
        self.grafica+="\nrankdir=TB;\n"
        self.grafica+="node[color=\"blue\",style=\"rounded,filled\",fillcolor=lightgray, shape=record];\n"
         
        self.Graficar2(self.Raiz)
        
        self.Graficar3(self.Raiz)
        
        self.grafica+="\n}\n"
        
        file.write(self.grafica)
        file.close()
        os.system("dot -Tpng BTree.dot -o BTree-"+tipo+".png")
        os.startfile("BTree"+tipo+".png")

    def Graficar2(self, pagina):
        contador=0
        if(pagina!=None):
            self.nodos=0
            for i in range(pagina.getCuenta()):
                
                if(pagina.getCodigo(i)!=None):
                    if(pagina.getCodigo(i)!=""):
                        self.nodos+=1
                        if(i!=0):
                            self.grafica+="|"
                        if(self.nodos==1):
                            self.grafica+="\nNodo"+pagina.getCodigo(i)+"[label=\"<f0> |"
                        
                        if(i==0):
                            self.grafica+="<f"+str(i+1)+">"+str(pagina.getCodigo(i))+"\\n"+pagina.getPais(i) + "|<f"+str(i+2)+"> "
                            contador=3
                        else:
                            self.grafica+="<f"+str(contador)+">"+str(pagina.getCodigo(i))+"\\n"+pagina.getPais(i) + "|<f"+str(contador+1)+"> "
                            contador+=2                        
                        
                        if(i==pagina.getCuenta()-1):
                            contador=0
                            self.grafica+=" \",group=0];\n"
            
            self.Graficar2(pagina.getApuntador(0))
            self.Graficar2(pagina.getApuntador(1))
            self.Graficar2(pagina.getApuntador(2))
            self.Graficar2(pagina.getApuntador(3))
            self.Graficar2(pagina.getApuntador(4))

    def Graficar3(self, pagina):
        if(pagina!=None):
            
                if(pagina.getCodigo(0)!=None):
                    if(pagina.getCodigo(0)!=""):
                        if((pagina.getApuntador(0)!=None) & (pagina.getApuntador(0).getCodigo(0)!=None)):
                            self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f0->"+"Nodo"+str(pagina.getApuntador(0).getCodigo(0))
                            print(self.grafica)
                            if((pagina.getApuntador(1)!=None) & (pagina.getApuntador(1).getCodigo(0)!=None)):
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f2->"+"Nodo"+str(pagina.getApuntador(1).getCodigo(0))
                            if((pagina.getApuntador(2)!=None) & (pagina.getApuntador(2).getCodigo(0)!=None)):
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f4->"+"Nodo"+str(pagina.getApuntador(2).getCodigo(0))
                            if((pagina.getApuntador(3)!=None) & (pagina.getApuntador(3).getCodigo(0)!=None)):
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f6->"+"Nodo"+str(pagina.getApuntador(3).getCodigo(0))
                            if((pagina.getApuntador(4)!=None) & (pagina.getApuntador(4).getCodigo(0)!=None)):
                                self.grafica+="\nNodo"+str(pagina.getCodigo(0))+":f8->"+"Nodo"+str(pagina.getApuntador(4).getCodigo(0))
            
                self.Graficar3(pagina.getApuntador(0))
                self.Graficar3(pagina.getApuntador(1))
                self.Graficar3(pagina.getApuntador(2))
                self.Graficar3(pagina.getApuntador(3))
                self.Graficar3(pagina.getApuntador(4))

    def getPaisM1(self, codigo):
        paisB=""
        self.getPaisM(self.Raiz,codigo)
        paisB=self.pais
        pais=""
        return paisB

    def getPaisM(self, pagina, codigo):
        
        if(pagina!=None):
            
            for i in range(pagina.getCuenta()):
                if(pagina.getCodigo(i)!=None):
                    if(pagina.getCodigo(i)!=""):
                        if(pagina.getCodigo(i)==(codigo)):
                            self.pais= pagina.getPais(i)
                            self.creditos= pagina.getCreditos(i)
                            self.Prerequisitos= pagina.getPrerequisitos(i)
                            self.Obligatorio= pagina.getObligatorio(i)
            
            self.getPaisM(pagina.getApuntador(0),codigo)
            self.getPaisM(pagina.getApuntador(1),codigo)
            self.getPaisM(pagina.getApuntador(2),codigo)
            self.getPaisM(pagina.getApuntador(3),codigo)
            self.getPaisM(pagina.getApuntador(4),codigo)
