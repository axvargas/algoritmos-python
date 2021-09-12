'''
Created Date: Saturday September 11th 2021 7:47:14 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 7:50:01 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años')
    
    def avanzar(self):
        print(f'{self.nombre} está avanzando caminando')

class Ciclista(Persona):
    def __init__(self, nombre, edad, n_bicicleta):
        super().__init__(nombre, edad)
        self.n_bicicleta = n_bicicleta

    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años y mi número de bicicleta es {self.n_bicicleta}')

    def avanzar(self):
        print(f'{self.nombre} está avanzando en la bicicleta {self.n_bicicleta}')

def main():
    persona = Persona('Andrés', 21)
    persona.saludar()
    persona.avanzar()
    ciclista = Ciclista('Richard', 28, '123')
    ciclista.saludar()
    ciclista.avanzar()

if __name__ == "__main__":
    main()
