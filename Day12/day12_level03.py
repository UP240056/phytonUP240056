import random

# Ej. 1

def shuffle_list(lista):
    lista_copiada = lista.copy()
    random.shuffle(lista_copiada)
    return lista_copiada

# Ej. 2

def numeros_aleatorios_unicos():
    numeros = list(range(10))
    numeros_mezclados = shuffle_list(numeros)
    return numeros_mezclados[:7]
