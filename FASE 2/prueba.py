primos = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

class NodoCont:
    def __init__(self, carnet):
        self.carnet = carnet
        self.anotaciones = None

class TablaHash:
    def __init__(self, tamaño):
        self.Hash = None
        self.tamaño = tamaño
        self.minimo = 0
        self.agregados = 0
        self.iniciar()

    def iniciar(self):
        self.agregados = 0
        self.minimo = (self.tamaño/2)+0.5
        Newtable = [None]*self.tamaño

        self.Hash = Newtable

    def cargarInf(self, data, infor):
        posicion = self.FunHash(data)
        try:
            while(data!=self.Hash[posicion].carnet):
                if(self.Hash[posicion]!=None):
                    posicion = self.ColsicionHash(data, posicion)
        
            self.Hash[posicion].anotaciones = infor
        except:
            print("El dato no existe")

    def agregar(self, data):
        if(data!=None):
            posicion = self.FunHash(data.carnet)
            it1 = 0
            it2 = 0
            if(posicion<self.tamaño):
                while(self.Hash[posicion] != None):
                    if(it1<4):
                        it1+=1    
                        posicion = self.ColsicionHash(data.carnet, posicion)
                        it2+=1
                    elif(posicion<self.tamaño-1) & (it1>=4):
                        posicion +=1
                    elif(posicion==self.tamaño-1):
                        posicion = 0
            else:
                posicion = 0

            self.Hash[posicion] = data
            self.agregados+=1
            self.rehashing()

    def FunHash(self,data):
        return data % self.tamaño

    def ColsicionHash(self, data, i):
        return (data +(i*i)) % self.tamaño

    def Divisibilidad(self, ta):
        for i in range(0,len(primos)):
            if (int(ta)==int(primos[i])):
                return primos[i+1]
                
    def rehashing(self):
        if(self.agregados >= self.minimo):
            copyarray = self.Hash

            tamañoAnterior = self.tamaño

            Mod = self.Divisibilidad(self.tamaño) 
            
            self.tamaño = Mod

            self.iniciar()

            for i in range(0,tamañoAnterior):
                if(copyarray[i] != -1):
                        self.agregar(copyarray[i])

    def imprimir(self):
        for i in range(0,len(self.Hash)):
            if(self.Hash[i]!=None):
                print(str(i)+" -> " + str(self.Hash[i].carnet)+": "+str(self.Hash[i].anotaciones))

if __name__ == '__main__':
    Ha = TablaHash(7)
    Ha.agregar(NodoCont(201801287))
    Ha.agregar(NodoCont(201800918))
    Ha.agregar(NodoCont(201800926))
    Ha.agregar(NodoCont(201801289))
    Ha.agregar(NodoCont(201709020))
    Ha.agregar(NodoCont(201709051))
    Ha.agregar(NodoCont(201902209))
    Ha.agregar(NodoCont(201801369))
    Ha.agregar(NodoCont(201801619))
    Ha.agregar(NodoCont(201902210))
    Ha.agregar(NodoCont(201902781))
    Ha.agregar(NodoCont(201907636))
    Ha.agregar(NodoCont(201908075))
    Ha.agregar(NodoCont(201902745))
    Ha.agregar(NodoCont(201908359))
    Ha.agregar(NodoCont(201801627))
    Ha.agregar(NodoCont(201503059))
    Ha.agregar(NodoCont(201755064))
    Ha.cargarInf(201908359, "Hola que hace")
    Ha.cargarInf(201755064, "Hola que hace")
    Ha.cargarInf(201801369, "Hola que hace")
    Ha.imprimir()