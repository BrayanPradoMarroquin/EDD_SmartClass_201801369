from cryptography.fernet import Fernet

file = open('key.key', 'rb')
hola = file.read()
file.close()

keygen = Fernet(hola)

prueba = "201907636"
data = keygen.encrypt(prueba.encode())

print(data)


print(keygen.decrypt(data).decode())