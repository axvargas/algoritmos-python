'''
Created Date: Saturday September 11th 2021 6:06:56 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 6:21:01 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''


class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        return ((self.x - otra_coordenada.x)**2 + (self.y - otra_coordenada.y)**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"


def main():
    coordenada1 = Coordenada(1, 2)
    coordenada2 = Coordenada(3, 4)
    print(coordenada1.distancia(coordenada2))
    print(coordenada1)
    print(isinstance(coordenada1, Coordenada))


if __name__ == "__main__":
    main()
