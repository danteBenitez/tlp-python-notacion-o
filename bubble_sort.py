from typing import TypeVar

T = TypeVar('T')

def bubble_sort_asc(lst: list[int]) -> list[T]:
    """
        Retorna una nueva lista ordenada de menor a mayor con el algoritmo Bubble Sort.

        :param lst: Lista de elementos a ordenar.
        :return: Lista ordenada de menor a mayor.
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def bubble_sort_with(n: int) -> list[int]:
    """
        Realiza una ordenación de una lista de tamaño `n` con el algoritmo Bubble Sort.
    """
    lst = [n - i for i in range(n)]
    return bubble_sort_asc(lst)
