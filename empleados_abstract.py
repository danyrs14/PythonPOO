"""
Crea una clase abstracta Empleado con:
Atributos: nombre, apellido, salario.
Métodos abstracto: calcular_bono().
Crea dos clases concretas:
EmpleadoTiempoCompleto: el bono es 20% del salario.
EmpleadoMedioTiempo: el bono es 10% del salario.
Instancia ambos tipos de empleados y muestra su salario total incluyendo el bono.
"""
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    @abstractmethod
    def calcular_bono(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido, salario)

    def calcular_bono(self):
        bono_empleado = self.salario * 0.20
        salario_bono = bono_empleado + self.salario
        return ("El bono es ", bono_empleado, "y el salario completo es ", salario_bono)

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido, salario)

    def calcular_bono(self):
        bono_midempleado = self.salario * 0.10
        salario_bono = bono_midempleado + self.salario
        return ("El bono es ", bono_midempleado, "Y el salario completo es ", salario_bono)

des = str(input("¿Eres empleado de tiempo completo (A) o de medio tiempo (B)?\n"))

if des == "A":
    name = str(input("Ingresa el nombre del empleado: "))
    apellid = str(input("Ingresa el apellido: "))
    salari = float(input("Ingresa el salario: "))
    comp = EmpleadoTiempoCompleto(name, apellid, salari)
    print(comp.calcular_bono())
elif des == "B":
    name = str(input("Ingresa el nombre del empleado: "))
    apellid = str(input("Ingresa el apellido: "))
    salari = float(input("Ingresa el salario: "))
    mid = EmpleadoMedioTiempo(name, apellid, salari)
    print(mid.calcular_bono())
else:
    "No existe ese tipo de empleado"