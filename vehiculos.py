"""
Crea una clase abstracta Vehiculo con:
Atributos: marca, modelo, velocidad.
Métodos abstractos: acelerar(cantidad) y frenar(cantidad).
Crea dos clases concretas que hereden de Vehiculo:
Carro: implementa acelerar y frenar, y un métodos extra abrir_cajuela().
Motocicleta: implementa acelerar y frenar, y un métodos extra hacer_caballito().
Instancia un Carro y una Motocicleta y prueba todos sus métodos.
"""

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    @abstractmethod
    def acelerar(self, cantidad):
        pass

    @abstractmethod
    def frenar(self, cantidad):
        pass

class Carro(Vehiculo):
    def __init__(self, marca, modelo, velocidad):
        super().__init__(marca, modelo, velocidad)

    def acelerar(self, cantidad):
        acel = self.velocidad + cantidad
        return acel

    def frenar(self, cantidad):
        fren = self.velocidad - cantidad
        return fren

    def abrir_cajuela(self):
        return print("Cajuela Abierta")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad):
        super().__init__(marca, modelo, velocidad)

    def acelerar(self, cantidad):
        acel = self.velocidad + cantidad
        return acel

    def frenar(self, cantidad):
        fren = self.velocidad - cantidad
        return fren

    def hacer_caballito(self):
        return print("Modo caballito en curso")

name = str(input("Ingrese el nombre del vehiculo: "))
model = str(input("Ingrese el modelo del vehiculo: "))
vel = int(input("Ingrese el velocidad del vehiculo en Km/h: "))

car = Carro(name, model, vel)
print(car.marca, car.modelo, car.velocidad)

des = str(input("Que quieres hacer Acelerar (A), Frenar (B), Abrir Cajuela (C)\n"))

if des == "A":
    kilometros = int(input("Ingrese la cantidad de kilometros a acelerar: "))
    print(car.acelerar(kilometros))
elif des == "B":
    kilometrosf = int(input("Ingrese la cantidad de kilometros a acelerar: "))
    print(car.frenar(kilometrosf))
elif des == "C":
    car.abrir_cajuela()
else:
    "Opcion no valida"

namemoto = str(input("Ingrese el nombre del motocicleta: "))
modelmoto = str(input("Ingrese el modelo del motocicleta: "))
velmoto = int(input("Ingrese el velocidad del motocicleta: "))

moto = Motocicleta(namemoto, modelmoto, velmoto)
print(moto.marca, moto.modelo, moto.velocidad)

des = str(input("Que quieres hacer Acelerar (A), Frenar (B), Caballito (C)\n"))

if des == "A":
    km = int(input("Ingrese la cantidad de kilometros a acelerar: "))
    print(car.acelerar(km))
elif des == "B":
    kmf = int(input("Ingrese la cantidad de kilometros a acelerar: "))
    print(car.frenar(kmf))
elif des == "C":
    moto.hacer_caballito()
else:
    "Opcion no valida"