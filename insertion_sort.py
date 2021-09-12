'''
Created Date: Saturday September 11th 2021 9:42:18 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 9:42:56 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import random as rd


def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j] < lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input("Ingrese el tamaño de la lista: "))
    print("Generando lista...")
    arr = [rd.randint(0, 100) for _ in range(tamano_de_lista)]
    print("Lista generada: ", arr)
    print(insertion_sort(arr))
