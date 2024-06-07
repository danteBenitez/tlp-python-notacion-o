import random
from typing import TypeVar

T = TypeVar("T")

def array_access(arr: list[T], idx: int) -> T:
    """
        Retorna el acceso a un índice de un arreglo.

        :param arr: Arreglo.
        :type str
    """
    return arr[idx]

def array_access_with(n: int) -> str:
    """
        Realiza un acceso a un índice de un arreglo de tamaño `n`.
    """
    arr = [str(i) for i in range(n)]
    index = random.randint(0, n - 1)
    return array_access(arr, index)