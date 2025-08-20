#encapsulamiento
class Usuario:
    def __init__(self, nombre, apellido, contrasenia, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.correo = correo
        self.telefono = telefono

    def obtener_telefono(self):
        return self.telefono

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def encriptarContrasenia(self, contrasenia):
        pass

    def desencriptarContrasenia(self, contrasenia):
        pass

user1 = Usuario(nombre="Daniel", apellido="Rodsan", contrasenia="root", correo="ejsdfj@jndskf.com", telefono="5512345678")
print(user1.actualizar_telefono(55780945389))
print(user1.obtener_telefono())