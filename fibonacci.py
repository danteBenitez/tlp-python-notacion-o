def fibonacci(n: int) -> int:
    """
        Retorna el n-ésimo número de la serie de Fibonacci.

        :param n: Posición en la serie de Fibonacci a calcular.
        :type int
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)