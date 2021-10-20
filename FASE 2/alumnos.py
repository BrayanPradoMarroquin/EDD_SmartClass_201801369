from ESTRUCTURAS_.ArbolAVL import ArbolAVL_
from ESTRUCTURAS_.ARBOLB_.BTree import BTree
from cryptography.fernet import Fernet

Alumnos_ = ArbolAVL_()
Pensum = BTree()
file = open('key.key', 'rb')
key = file.read()
file.close()

def encryp(data):
    print("Hola")

def decryp(data):
    print("adios")