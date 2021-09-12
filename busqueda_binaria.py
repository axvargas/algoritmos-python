'''
Created Date: Saturday September 11th 2021 9:15:40 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 9:32:42 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import random as rd
def busqueda_binaria(lista, elemento, steps):
    steps += 1
    print(f"Buscando {elemento} en la lista {lista}")
    if len(lista) == 0:
        return False, steps
    mitad = len(lista) // 2
    if lista[mitad] == elemento:
        return True, steps
    elif elemento < lista[mitad]:
        return busqueda_binaria(lista[:mitad], elemento, steps)
    else:
        return busqueda_binaria(lista[mitad+1:], elemento, steps)

if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño será la lista? "))
    objetivo = int(input("Que número quieres encontrar? "))
    lista = sorted([rd.randint(0, 100) for _ in range(tamano_de_lista)]) # Genera una lista de números aleatorios MUST BE SORTED
    print(lista)
    encontrado, steps = busqueda_binaria(lista, objetivo, 0)
    print(f"El elemento {objetivo} {'está' if encontrado else 'no está'} en la lista")
    print(f"El algoritmo usó {steps} pasos")