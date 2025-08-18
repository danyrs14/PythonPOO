"""
Crea una clase abstracta CuentaBancaria con:
Atributos: titular, numero_cuenta, saldo.
Métodos abstractos: depositar(monto) y retirar(monto).
Crea una clase CuentaAhorro que herede de CuentaBancaria y:
Implementa depositar y retirar.
Agrega un métodos calcular_interes(tasa) que devuelva el saldo con interés.
Instancia una CuentaAhorro, deposita, retira y calcula interés.
"""

from abc import ABC, abstractmethod

class CuentaBancaria(ABC):#clase abstracta
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    @abstractmethod#metodo abstracto
    def depositar(self, monto):
        pass

    @abstractmethod#metodo abstracto
    def retirar(self, monto):
        pass

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, numero_cuenta, saldo):
        super().__init__(titular, numero_cuenta, saldo)

    def depositar(self, monto):
        deposito = self.saldo + monto
        return deposito

    def retirar(self, monto):
        retiro = self.saldo - monto
        return retiro

    def calcular_interes(self, tasa, anios):
        interes = self.saldo * tasa * anios
        return interes

nombre = str(input("Ingrese el nombre: "))
num_cuenta = int(input("Ingrese el numero de cuenta: "))
saldo = float(input("Ingrese la saldo: "))

acount = CuentaAhorro(nombre, num_cuenta, saldo)

print("Titular:", acount.titular, "Numero de Cuenta:", acount.numero_cuenta, "Saldo:",acount.saldo)

opcion = str(input("Deseas depositar (A) o retirar (B) o calcular interes (C)\n"))

if opcion == "A":
    mount = float(input("Ingresa el monto a depositar: "))
    print("Saldo final despues del deposito:", acount.depositar(mount))
elif opcion == "B":
    mount = float(input("Ingresa el monto a retirar: "))
    print("Saldo final despues del retiro:", acount.retirar(mount))
elif opcion == "C":
    tason = float(input("Ingresa la tasa en %: p.e 100% -> 1.0 y 50% -> 0.5\n"))
    years = int(input("Ingresa los años que llevas invirtiendo: "))
    print("La tasa de interes en tu cuenta es de ", acount.calcular_interes(tason, years))
else:
    print("Opcion no valida")


