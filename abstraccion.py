from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class UsuarioBase(ABC):#heredamos la clase ABC

    def __init__(self, nombre, apellido, correo, contrasenia, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.telefono = telefono

    @abstractmethod#es una funcion y un decorador y va a englobar caracteristicas especiales de abstractmethod
    def encriptarContrasenia(self, contrasenia):
        pass

    @abstractmethod
    def verificarContrasenia(self, contrasenia):
        pass

class UsuarioConcreto(UsuarioBase):

    def encriptarContrasenia(self, contrasenia):
        return encrypt(contrasenia, "secret")

    def verificarContrasenia(self, contrasenia):
        contrasenia_desencriptada = decrypt(self.contrasenia, "secret")
        return contrasenia_desencriptada == contrasenia

usuario = UsuarioConcreto(nombre="Daniel", apellido="Rodsan", correo="danyrs14@gmail.com", contrasenia="root", telefono="5578876132")

print(usuario.contrasenia)
print(usuario.verificarContrasenia("roo"))