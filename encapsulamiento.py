class Usuario:
    def __init__(self, nombre, apellido, contrasenia, correo, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contrasenia = self.__encriptar_contrasenia(contrasenia)
        self.__correo = correo
        self.__telefono = telefono

    # ======================
    # MÉTODOS GETTERS (obtener valores)
    # ======================
    def obtener_nombre(self):
        return self.__nombre

    def obtener_telefono(self):
        return self.__telefono

    def obtener_correo(self):
        return self.__correo

    # ======================
    # MÉTODOS SETTERS (modificar valores de forma controlada)
    # ======================
    def actualizar_telefono(self, nuevo_telefono):
        # aquí podrías validar que sea un número válido
        self.__telefono = nuevo_telefono

    def actualizar_correo(self, nuevo_correo):
        # aquí podrías validar que el correo tenga formato correcto
        self.__correo = nuevo_correo

    # ======================
    # MANEJO DE CONTRASEÑA (encapsulada)
    # ======================
    def __encriptar_contrasenia(self, contrasenia):
        # En este ejemplo simple solo invertimos la cadena
        # (en la vida real usarías hashlib o bcrypt)
        return contrasenia[::-1]

    def __desencriptar_contrasenia(self):
        # Revertimos el encriptado para obtener la contraseña original
        return self.__contrasenia[::-1]

    def verificar_contrasenia(self, contrasenia):
        return contrasenia == self.__desencriptar_contrasenia()


# ======================
# USO
# ======================
user1 = Usuario(
    nombre="Daniel",
    apellido="Rodsan",
    contrasenia="root",
    correo="daniel@mail.com",
    telefono="5512345678"
)

print(user1.obtener_nombre())       # ✅ accedemos al nombre con getter
print(user1.obtener_telefono())     # ✅ obtenemos el teléfono
user1.actualizar_telefono("5587654321")
print(user1.obtener_telefono())     # ✅ teléfono actualizado

print(user1.verificar_contrasenia("root"))   # ✅ True
print(user1.verificar_contrasenia("admin"))  # ❌ False
