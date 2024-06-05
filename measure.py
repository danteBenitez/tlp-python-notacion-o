import time

def measure_time(fn: callable, args):
    """
        Ejecuta una función y mide el tiempo que tarda en ejecutarse.
        Retorna el tiempo que tarda en ejecutarse la función.

        :param fn: Lista de funciones a ejecutar.
        :type callable

        :param args: Argumentos que se le pasan a las funciones.
        :type tuple
    """
    start = time.perf_counter()
    fn(*args)
    
    return time.perf_counter() - start
