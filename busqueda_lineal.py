import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # La complejidad algorítmica es de O(n)
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    list_size = int(input("De qué tamaño será la lista? "))
    objetivo = int(input("¿Qué número quieres encontrar? "))

    lista = [random.randint(0, 10) for i in range(list_size)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
