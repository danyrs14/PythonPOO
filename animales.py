"""
Crea una clase padre Animal con:
Atributos: nombre, edad
Métodos: emitir_sonido() que solo imprima "Sonido genérico".
Crea una clase hija Perro que herede de Animal y:
Tenga un nuevo atributo raza.
Sobrescriba el métodos emitir_sonido() para imprimir "Guau guau".
Crea una clase hija Gato que herede de Animal y:
Tenga un nuevo atributo color.
Sobrescriba el métodos emitir_sonido() para imprimir "Miau".
Crea instancias de Perro y Gato y llama sus métodos.
"""
#Clase padre
class Animal():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self):
        return "Sonido generico"

#calse hijo
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def emitir_sonido(self):
        return "Guau Guau"

#calse hijo
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def emitir_sonido(self):
        return "Miau"

name_dog = str(input("Nombre del perro: "))
edad_dog = str(input("Edad del perro: "))
raza_dog = str(input("Raza del perro: "))

#instancias
pastor = Perro(name_dog, edad_dog, raza_dog)
print(pastor.nombre)
print(pastor.edad)
print(pastor.raza)
print(pastor.emitir_sonido())

name_cat = str(input("Nombre del gato: "))
edad_cat = str(input("Edad del gato: "))
color_cat = str(input("Color del gato: "))

#instancias
cat = Gato(name_cat, edad_cat, color_cat)
print(name_cat)
print(edad_cat)
print(color_cat)
print(cat.emitir_sonido())