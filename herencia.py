'''
Created Date: Saturday September 11th 2021 6:56:47 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 7:44:56 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


def main():
    rectangulo = Rectangulo(5, 10)
    print(rectangulo.area())
    print(rectangulo.perimetro())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())
    print(cuadrado.perimetro())


if __name__ == "__main__":
    main()
