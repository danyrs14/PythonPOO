"""
Crea una clase Computadora con atributos: marca, procesador, ram, almacenamiento.
Agrega un métodos mostrar_info() que imprima todos los datos.
Crea una instancia y llama al métodos.
"""

class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def mostrar_info(self):
        return f"Marca: {self.marca}, Procesador: {self.procesador}, Ram: {self.ram}, Almacenamiento: {self.almacenamiento}"

marca_pc = str(input("Ingrese la marca de la computadora: "))
procesador_pc = str(input("Ingrese la procesador de la computadora: "))
ram_pc = int(input("Ingrese en GB la RAM de la computadora: "))
storage = int(input("Ingrese el almacenamiento en GB de la computadora: "))

pc = Computadora(marca_pc, procesador_pc, ram_pc, storage)
print(pc.mostrar_info())