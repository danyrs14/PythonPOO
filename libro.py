"""
Crea una clase Libro con atributos: titulo, autor, anio, genero.
Crea dos instancias y asigna valores a los atributos después de crearlas.
Muestra la información de cada libro en pantalla.
"""
#nombre clase
class Libro():
    #atributos
    titulo = ""
    autor = ""
    anio = ""
    genero = ""

name = str(input("Ingresa un titulo de un libro: "))
autor_libro = str(input("Ingresa el/la autor(a) del libro: "))
ano_libro = str(input("Ingresa el año del libro: "))
genero_libro = str(input("Ingresa el genero del libro: "))
#instancias
print("LIBRO 1")
libro1 = Libro()
libro1.titulo = name
libro1.autor = autor_libro
libro1.anio = ano_libro
libro1.genero = genero_libro
print("Titulo:",libro1.titulo)
print("Autor:",libro1.autor)
print("Año:",libro1.anio)
print("Genero:",libro1.genero)

name2 = str(input("Ingresa el nombre del libro: "))
autor_libro2 = str(input("Ingresa el/la autor(a) del libro: "))
ano_libro2 = str(input("Ingresa el año del libro: "))
genero_libro2 = str(input("Ingresa el genero del libro: "))
#instancias
print("LIBRO 2")
libro2 = Libro()
libro2.titulo = name2
libro2.autor = autor_libro2
libro2.anio = ano_libro2
libro2.genero = genero_libro2
print("Titulo:",libro2.titulo)
print("Autor:",libro2.autor)
print("Año:",libro2.anio)
print("Genero:",libro2.genero)

