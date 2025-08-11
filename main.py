#Ejemplo de una clase
#El nombre de la clase siempre tiene que empezar con Mayuscula ej, Hola, Usuario, Saludo
#A continuacion está la estructura basica de una clase
class Usuario():#NOMBRE
    #DATOS (atributos)
    nombre = ""
    apellido = ""
    correo = ""
    contrasena = ""

    #METODOS (funcionalidad)
    #en los metodos sus funciones deben tener self como parametro
    def encritarContrasena(self):
        pass
        return "encriptando..."

    def verificarContrasena(self):
        pass
        return "desencriptando..."

#Se crea una instancia de la clase usuario es decir una copia
#por lo que ahora usuario1 es igual a la clase usuario
usuario1 = Usuario()

#atraves de un punto podemos ingresar a sus metodos como en los siguientes ejemplos
usuario1.encritarContrasena()
usuario1.verificarContrasena()

#asi como tambien podemos acceder a sus atributos
print(usuario1.nombre)
print(usuario1.encritarContrasena())
usuario1.nombre = "Luis"
usuario1.apellido = "Rodriguez"

print("USUARIO 1")
print(usuario1.nombre)
print(usuario1.apellido)

usuario2 = Usuario()

usuario2.nombre = "Ernesto"
usuario2.apellido = "Diez de Sollano"

print("USUARIO 2")
print(usuario2.nombre)
print(usuario2.apellido)