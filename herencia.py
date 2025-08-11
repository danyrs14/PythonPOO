#Herencia (al menos 2 clases) clase padre y clase hijo
#clase base
class Vehiculo:
    #atributos dentro de un constructor
    def __init__(self,nombre, modelo, velocidad, anio):
        self.nombre = nombre
        self.modelo = modelo
        self.velocidad = velocidad
        self.anio = anio

    #metodos
    def darVelocidad(self, velocidad):
        self.velocidad += velocidad

    def reducir_velocidad(self, velocidad):
        self.velocidad -= velocidad

#clase hijo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad, anio, motor):
        super().__init__(marca, modelo, velocidad, anio)#actualizamos los atributos de la clase base
        self.motor = motor#creamos un nuevo atributo solo para esta clase

    def Wheelie(self):
        return "Haciendo el caballito"

#clase hijo
class Autobus(Vehiculo):
    def __init__(self, marca, modelo, velocidad, anio, motor, asientos):
        super().__init__(marca, modelo, velocidad, anio)
        self.motor = motor
        self.asientos = asientos

    def cargar_pasajeros(self, pasajeros):
        return f"Pasajeros a bordo {pasajeros}"

marca_carro = str(input("Ingrese el marca de la carro: "))
modelo_carro = str(input("Ingrese el modelo de la carro: "))
velocidad_carro = int(input("Ingrese el velocidad de la carro: "))
ano_carro = int(input("Ingrsa el año del carro: "))
motor_carro = str(input("Ingrese el motor de la carro: "))

moto = Motocicleta(marca_carro, modelo_carro, velocidad_carro, ano_carro, motor_carro)

print(moto.nombre)
print(moto.Wheelie())

marca_carro1 = str(input("Ingrese el marca de la Autobus: "))
modelo_carro1= str(input("Ingrese el modelo de la Autobus: "))
velocidad_carro1 = int(input("Ingrese el velocidad de la Autobus: "))
ano_carro1 = int(input("Ingrsa el año del Autobus: "))
motor_carro1 = str(input("Ingrese el motor de la Autobus: "))
asientos_carro1 = int(input("Ingrese el asientos: "))

camion = Autobus(marca_carro1, modelo_carro1, velocidad_carro1, ano_carro1, motor_carro1, asientos_carro1)
print(camion.cargar_pasajeros(asientos_carro1))