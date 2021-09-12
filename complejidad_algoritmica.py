'''
Created Date: Saturday September 11th 2021 7:59:42 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 8:18:24 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import time
import sys

sys.setrecursionlimit(10**6)

# factorial sin recursion
def factorial_loop(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":

    n = 3000
    
    print("Factorial sin recursion")
    t1 = time.time()
    factorial_loop(n)
    t2 = time.time()
    print(f"Tiempo de ejecucion: {t2-t1}")
    print("Factorial con recursion")
    t1_ = time.time()
    factorial(n)
    t2_ = time.time()
    print(f"Tiempo de ejecucion: {t2_-t1_}")