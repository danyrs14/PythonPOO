"""
Crea una clase Pelicula con atributos: nombre, director, duracion, clasificacion.
Agrega un métodos reproducir() que imprima "Reproduciendo <nombre>".
Crea una instancia, asigna los valores y llama al métodos.
"""

class Pelicula:
    nombre = ""
    director = ""
    duracion = ""
    clasificacion = ""

    def reproducir(self):
        #de esta manera se concatena los atributos en las clases
        return "Reproduciendo: " + self.nombre

name = str(input("Nombre de la Pelicula: "))
director = str(input("Director de la pelicula: "))
duracion = int(input("Duracion en min: "))
clasificacion = str(input("Clasificacion de la pelicula: "))
movile = Pelicula()
movile.nombre = name
movile.director = director
movile.duracion = duracion
movile.clasificacion = clasificacion
print("PELICULA 1")
print("Nombre: ", movile.nombre)
print("Director: ", movile.director)
print("Duracion: ", movile.duracion)
print("Clasificacion: ", movile.clasificacion)
print(movile.reproducir())
