"""
Crea una clase padre Dispositivo con:
Atributos: marca, modelo
Métodos: encender() que imprima "El dispositivo está encendido".
Crea una clase hija Smartphone que:
Añada un atributo sistema_operativo.
Tenga un métodos instalar_app(nombre_app) que imprima "Instalando <nombre_app>".
Crea una clase hija Laptop que:
Añada un atributo procesador.
Tenga un métodos compilar_codigo() que imprima "Compilando código...".
Crea un Smartphone y una Laptop y prueba sus métodos.
"""

#Clase padre
class Dispositivo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        return "El dispositivo esta encendido"

#Clase hija
class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo

    def instalar_app(self, nombre_app):
        return f"Instalando {nombre_app}"


#clase hija
class Laptop(Dispositivo):
    def __init__(self, marca, modelo, procesador):
        super().__init__(marca, modelo)
        self.procesador = procesador

    def compilar_codigo(self):
        return "Compilando codigo..."

#instancias
marca_celular = str(input("Marca del celular: "))
modelo_celular = str(input("Modelo del celular: "))
sistema_operativo = str(input("Sistema operativo del celular: "))
app = str(input("Ingresa una app a instalar: "))

celular = Smartphone(marca_celular, modelo_celular, sistema_operativo)

print("CELULAR")
print(celular.marca, celular.modelo, celular.sistema_operativo)
print(celular.encender())
print(celular.instalar_app(app))

marca_laptop = str(input("Marca del laptop: "))
modelo_laptop = str(input("Modelo del laptop: "))
procesador = str(input("Ingresa una procesador: "))

portatil = Laptop(marca_laptop, modelo_laptop, procesador)
print("LAPTOP")
print(portatil.marca, portatil.modelo, portatil.procesador)
print(portatil.encender())
print(portatil.compilar_codigo())

