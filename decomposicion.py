'''
Created Date: Saturday September 11th 2021 6:27:48 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 6:32:59 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
            
        self._estado = 'en marcha'

class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        pass