'''
Created Date: Saturday September 11th 2021 9:49:48 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 10:23:07 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import random as rd


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print(f"{L} {'*' * 5} {R}")
        
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print(f"L: {L} , R: {R}")
        print(f"arr: {arr}")
        print("-" *50)
    return arr


if __name__ == "__main__":
    tamano_de_lista = int(input("Ingrese el tamaño de la lista: "))
    print("Generando lista...")
    arr = [rd.randint(0, 100) for _ in range(tamano_de_lista)]
    print("Lista generada: ", arr)
    print(merge_sort(arr))