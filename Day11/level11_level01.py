import math
from typing import List, Union, Optional

# Ej. 1

def sumar_dos_numeros(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

# Ej. 2

def area_del_circulo(radio: float) -> float:
    return math.pi * radio * radio

# Ej. 3

def sumar_todos_los_numeros(*args: Union[int, float]) -> Union[int, float, str]:
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Todos los elementos deben ser números"
        total += num
    return total

# Ej. 4

def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# Ej. 5
def obtener_estacion(mes: str) -> str:
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

# Ej. 6

def calcular_pendiente(x1: float, y1: float, x2: float, y2: float) -> float:
    return (y2 - y1) / (x2 - x1)

# Ej. 7

def resolver_ecuacion_cuadratica(a: float, b: float, c: float) -> Optional[List[float]]:
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    elif discriminante == 0:
        return [-b / (2*a)]
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return [raiz1, raiz2]

# Ej. 8

def imprimir_lista(lista: List) -> None:
    for elemento in lista:
        print(elemento)

# Ej. 9

def invertir_lista(lista: List) -> List:
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# Ej. 10

def capitalizar_elementos_lista(lista: List[str]) -> List[str]:
    return [elemento.capitalize() for elemento in lista]

# Ej. 11

def agregar_elemento(lista: List, elemento) -> List:
    nueva_lista = lista.copy()
    nueva_lista.append(elemento)
    return nueva_lista

# Ej. 12

def eliminar_elemento(lista: List, elemento) -> List:
    nueva_lista = lista.copy()
    if elemento in nueva_lista:
        nueva_lista.remove(elemento)
    return nueva_lista

# Ej. 13

def suma_de_numeros(n: int) -> int:
    return sum(range(1, n+1))

# Ej. 14

def suma_de_impares(n: int) -> int:
    return sum(i for i in range(1, n+1) if i % 2 != 0)

# Ej. 15

def suma_de_pares(n: int) -> int:
    return sum(i for i in range(1, n+1) if i % 2 == 0)