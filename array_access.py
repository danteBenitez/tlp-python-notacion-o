def array_access(arr: list[str], idx: int) -> str:
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
    return array_access(arr, n - 1)