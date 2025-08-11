"""
Crea una clase Avion con atributos: compania, modelo, capacidad, destino.
Agrega un métodos despegar() que imprima "El avión con destino a <destino> está despegando".
Crea una instancia y prueba el métodos.
"""

class Avion:
    def __init__(self, compania, modelo, capacidad, destino):
        self.compania = compania
        self.modelo = modelo
        self.capacidad = capacidad
        self.destino = destino

    def despegar(self):
        return f"El avion con destino a {self.destino} esta despegando"

compa = str(input("Compania: "))
model = str(input("Modelo: "))
cap = str(input("Capacidad: "))
dest = str(input("Destino: "))

aeroplane = Avion(compa, model, cap, dest)
print(aeroplane.despegar())