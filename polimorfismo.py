"Polimorfismo (muchas formas)"

#tenemos una clase padre o clase madre
class Shape:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    #tenemos un metodo general que de momento no hace nada
    #pero sirve como base para las clases hijas que hereden
    #de la misma forma que lo haciamos en la abstraccion
    def draw(self):
        pass

#creamos una clase hija que herede ciertos atributos del padre
#y aparte le añadimos un atributo propio
class Circulo(Shape):
    def __init__(self, x, y, radius):
        #si se pone raius*2 dos veces es porque la clase padre esta diseñada para tener largo y ancho
        super().__init__(x, y, radius*2, radius*2)
        self.radius = radius

    #le damos un uso a draw  para que lo implemente de la forma en la que lo necesita
    def draw(self):
       return print(f"Imprimiendo la forma del circulo: {self.x}, {self.y}, y su radio es {self.radius}")

class Triangulo(Shape):
    def __init__(self, x, y, height, base):
        super().__init__(x, y, height, base)
        self.base = base

    #asimismo le damos un uso segun las necesidades
    def draw(self):
        return print(f"Imprimiendo un triangulo en {self.x}, {self.y}, y su base es {self.base} y su altura es {self.height}")

class Rectangulo(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)

    def draw(self):
        return print(f"Imprimiendo un rectangulo con sus medidas {self.x}, {self.y}, y su largo es {self.height} y su alto es {self.width}")

circulo = Circulo(50, 50, 25)
triangulo = Triangulo(100, 100, 200, 200)
rectangulo = Rectangulo(300, 200, 200, 100)

#circulo.draw()
#triangulo.draw()
#rectangulo.draw()

## o bien se puede imprimir de esta manera

formas = [circulo, triangulo, rectangulo]

for forma in formas:
    forma.draw()
