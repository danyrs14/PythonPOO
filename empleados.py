"""
Crea una clase padre Empleado con:
Atributos: nombre, salario
Métodos: mostrar_info() que imprima el nombre y salario.
Crea una clase hija Gerente que:
Añada un atributo departamento.
Tenga un métodos dirigir() que imprima "Dirigiendo el departamento de <departamento>".
Crea una clase hija Vendedor que:
Añada un atributo comision.
Tenga un métodos vender() que imprima "Vendiendo con comisión del <comision>%".
Crea un Gerente y un Vendedor y muestra sus datos.
"""

#clase padre
class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, salario: {self.salario}"

#clase hija
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def dirigir(self):
        return f"Dirigiendo el departamento {self.departamento}"

#clase hija
class Vendedor(Empleado):
    def __init__(self, nombre, salario, comision):
        super().__init__(nombre, salario)
        self.comision = comision

    def vender(self):
        return f"Vendiendo con comision del {self.comision}%"

name_gerente = str(input("Nombre del gerente: "))
salario_gerente = float(input("Salario del gerente: "))
comision_gerente = str(input("Departamento del gerente: "))

#instancia
geren = Gerente(name_gerente, salario_gerente, comision_gerente)
print("GERENTE")
print(geren.mostrar_info(), geren.departamento)
print(geren.dirigir())

name_vendedor = str(input("Nombre del vendedor: "))
salario_vendedor = float(input("Salario del vendedor: "))
comision_vendedor = float(input("Comision del vendedor: "))

#intanscia
vendor = Vendedor(name_vendedor, salario_vendedor, comision_vendedor)
print("VENDEDOR")
print(vendor.mostrar_info(), vendor.comision)
print(vendor.vender())
