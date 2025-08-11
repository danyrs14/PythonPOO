class Usuario2():#NOMBRE
    #este metodo se llama constructor de la clase
    def __init__(self, nombre, apellido, correo, contrasena, telefono):
        #ademas de self, tambien ponemos como atributo lo que vamos a recibir de parametros
        # DATOS (atributos)
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.telefono = telefono
        #ya aca abajo con los atributos se denominan de la siguiente forma self.<nombre> = <parametro>

    #METODOS (funcionalidad)
    #en los metodos sus funciones deben tener self como parametro
    def encritarContrasena(self):
        return "encriptando..."

    def verificarContrasena(self):
        return "desencriptando..."

print("USUARIO 1")
#ahora ya como la clase tiene parametros al momento de instanciarla necesitamos inicializar los parametros
user1 = Usuario2(nombre="Daniel", apellido="Rodsan", correo="dani@famao", contrasena="sfasfasf", telefono="5512345678")
#para usar o imprimir los valores de los parametros se imprimen de la siguiente manera
print(user1.nombre)
print(user1.apellido)

print("USUARIO 2")
user2 = Usuario2(nombre="Nala", apellido="Leona", correo="ijnivd@ijcs.com", contrasena="sfkq", telefono="5512345678")
print(user2.nombre)
print(user2.apellido)