import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__":
    tamaño_de_lista = int(input("de que tamano es la lista"))
    objetivo = int(input("Que numero quieres econtrar?: "))

    lista = [random.randint(0,100) for i in range(tamaño_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f"El elemento {objetivo} {'esta' if encontrado else 'no esta'} en la lista")
