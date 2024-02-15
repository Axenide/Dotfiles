# This script is just for sorting the packages alphabetically. :)

def ordenar_lista_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lista = archivo.readlines()

    lista = [elemento.strip() for elemento in lista]

    lista_ordenada = sorted(lista)

    with open(nombre_archivo, 'w') as archivo:
        for elemento in lista_ordenada:
            archivo.write(elemento + '\n')

    print("La lista ha sido ordenada alfabéticamente y actualizada en el archivo.")

ordenar_lista_archivo("packages.txt")
ordenar_lista_archivo("personal.txt")
