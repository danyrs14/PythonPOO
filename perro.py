"""
Crea una clase Perro con atributos: nombre, raza, edad.
Agregas un métodos ladrar() que imprima "Guau!".
Crea dos instancias, asigna atributos y llama al métodos.
"""
class Perro:
    nombre = ""
    raza = ""
    edad = ""

    def ladrar(self):
        return f'El perro {self.nombre} dice Guau!'

nombre_perro = str(input("Nombre del perro: "))
raza_perro = str(input("Raza del perro: "))
edad_perro = str(input("Edad: "))

pastor = Perro()
pastor.nombre = nombre_perro
pastor.raza = raza_perro
pastor.edad = edad_perro

print("PERRO 1")
print("Nombre del Perro: ",pastor.nombre)
print("Raza del Perro: ",pastor.raza)
print("Edad: ",pastor.edad)

print(pastor.ladrar())

nombre_perro2 = str(input("Nombre del perro: "))
raza_perro2 = str(input("Raza del perro: "))
edad_perro2 = str(input("Edad: "))

grande = Perro()
grande.nombre = nombre_perro2
grande.raza = raza_perro2
grande.edad = edad_perro2

print("PERRO 2")
print("Nombre del Perro: ",grande.nombre)
print("Raza del Perro: ",grande.raza)
print("Edad: ",grande.edad)

print(grande.ladrar())
