# Extráido de https://github.com/danteBenitez/tlp-python-busqueda/blob/main/linear_search.py
from typing import TypeVar
import random

T = TypeVar('T')

def linear_search(lst: list[T], target: T) -> int:
    """
        Busca el elemento `target` en la lista `lst` y devuelve su índice si lo encuentra.

        :param lst: Lista en la que se buscará el elemento.
        :type list[T]

        :param target: Elemento a buscar en la lista.
        :type T

        :return: Índice del elemento `target` en la lista `lst` si lo encuentra, -1 en caso contrario.
    """
    # Por cada elemento en la lista...
    for i, elem in enumerate(lst):
        # Si el elemento es igual al objetivo...
        if elem == target:
            # Devolver el índice del elemento.
            return i
    # Por convención, retornamos -1 cuando no se encuentra.
    return -1

def linear_search_with(n: int) -> int:
    """
        Realiza una búsqueda lineal en una lista de tamaño `n`.
    """
    lst = list(range(n))
    target = lst[random.randint(0, n - 1)]
    return linear_search(lst, target)