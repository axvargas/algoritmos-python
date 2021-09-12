'''
Created Date: Saturday September 11th 2021 9:35:44 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 9:40:56 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import random as rd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    tamano_de_lista = int(input("Ingrese el tamaño de la lista: "))
    print("Generando lista...")
    arr = [rd.randint(0, 100) for _ in range(tamano_de_lista)]
    print("Lista generada: ", arr)
    print(bubble_sort(arr))