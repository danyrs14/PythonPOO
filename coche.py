"""
Crea una clase Coche con atributos: marca, modelo, color, velocidad.
Agrega un métodos acelerar() que sume 20 a la velocidad y lo imprima.
Crea dos instancias con datos distintos y prueba el métodos.
"""
class Coche:
    def __init__(self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def acelerar(self):
        resultado = self.velocidad + 20
        return resultado

marca_coche = str(input("Ingrese el marca de la coche: "))
modelo_coche = str(input("Ingrese el modelo de la coche: "))
color_coche = str(input("Ingrese el color de la coche: "))
velocidad_coche = int(input("Ingrese el velocidad de la coche: "))

auto = Coche(marca_coche, modelo_coche, color_coche, velocidad_coche)
print(auto.marca, auto.modelo, auto.color, auto.velocidad)
print(auto.acelerar())