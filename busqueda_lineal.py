'''
Created Date: Saturday September 11th 2021 9:04:17 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 9:27:57 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import random as rd
def busqueda_lineal(lista, objetivo):
    match = False
    posicion = -1
    steps = 0
    for i in range(len(lista)):
        steps += 1
        if lista[i] == objetivo:
            match = True
            posicion = i
            break
    return match, posicion, steps

if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño será la lista? "))
    objetivo = int(input("Que número quieres encontrar? "))

    lista = [rd.randint(0, 100) for _ in range(tamano_de_lista)]
    print(f"Lista generada: {lista}")

    encontrado, posicion, steps = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo} {f"está en la posición {posicion}" if encontrado else "no está"}')
    print(f'El algoritmo tomo {steps} pasos')