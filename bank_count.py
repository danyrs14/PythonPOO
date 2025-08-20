"""
Ejercicio 1: Cuenta bancaria
Crea una clase CuentaBancaria con los siguientes atributos:
__saldo (privado)
__titular (privado)
Y métodos:
depositar(monto) que aumente el saldo.
retirar(monto) que reste el saldo, pero solo si hay suficiente dinero.
consultar_saldo() que muestre el saldo actual.
⚡ Restricción: no se puede modificar el saldo directamente desde fuera de la clase, solo con los métodos.
"""

class CuentaBancaria:
    def __init__(self, saldo, titular):
        self.__saldo = saldo#atributos privados
        self.__titular = titular#atributos privados

    #obtener los valores GET
    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular

    #modificar los datos SET
    def depositar(self, monto):
        dep = self.obtener_saldo() + monto
        return dep

    def retirar(self, monto):
        ret = self.obtener_saldo() - monto
        return ret

sald = float(input("Ingresa el saldo: "))
tit = str(input("Ingresa el titular: "))

account = CuentaBancaria(sald, tit)
print(account.obtener_titular())#llamamos al get para que pueda imprimir sino lo llamamos y llamamos al atributo no va a obtener nada

des = str(input("Depositar (A) or Retirar (R): "))
if des == "A":
    mont = float(input("Ingresa el monto: "))
    print(account.depositar(mont))
elif des == "R":
    mont = float(input("Ingresa el monto: "))
    print(account.retirar(mont))
