import sys
import time

#implementación iterativa 

def factorial(n):
    respuesta = 1
    while n>1:
        respuesta *=n 
        n -= 1
    return respuesta

#implementación recursivo 

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)

if __name__ == "__main__":
    n = 1000

    comienzo = time.time()
    print(factorial(n))
    final = time.time()
    print(final - comienzo)


    comienzo_r = time.time()
    print(factorial_r(n))
    final_r = time.time()
    print(final_r - comienzo_r)