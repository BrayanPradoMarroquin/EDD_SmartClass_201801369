import hashlib

mensaje = "Hola Mundo"
contraseña = hashlib.sha256(mensaje.encode("utf-8"))
print(contraseña.hexdigest())