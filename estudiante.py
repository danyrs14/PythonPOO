"""
Crea una clase Estudiante con atributos privados:
__nombre
__calificacion
La clase debe permitir:
Un métodos asignar_calificacion(nota) que solo acepte números entre 0 y 10.
Un métodos obtener_calificacion() que muestre la calificación.
Un métodos aprobado() que devuelva True si la nota es mayor o igual a 6, de lo contrario False.
"""

class Estudiante:
    def __init__(self, nombre, calificacion):
        self.__nombre = nombre
        self.__calificacion = calificacion

    #getters para acceder a su informacion
    def obtener_nombre(self):
        return self.__nombre

    def obtener_calificacion(self):
        return self.__calificacion

    def asignar_calificacion(self, cantidad):
        return self.__calificacion + cantidad

    def aproado(self):
        score = 6
        if self.__calificacion >= score:
            return True
        else:
            return False

est = Estudiante(nombre="Daniel", calificacion=10)
print(est.obtener_nombre())
print(est.obtener_calificacion())
print(est.asignar_calificacion(0))
print(est.aproado())