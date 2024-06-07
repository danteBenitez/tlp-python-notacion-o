import numpy as np

import matplotlib.pyplot as plt
from binary_search import binary_search_with
from fibonacci import fibonacci
from bubble_sort import bubble_sort_with
from linear_search import linear_search_with
from measure import measure_time

from array_access import array_access_with

N_VALUES = [i for i in range(1, 30)]

def measure_times_for(fn: callable, n_values: np.ndarray) -> np.ndarray:
    """
        Mide el tiempo que le toma a `fn` ser llamada con cada valor de `n_values`.

        :param fn: Función a medir.
        :type callable

        :param n_values: Valores de `n` con los que se llamará a `fn`.
        :type np.ndarray

        :return: Arreglo con los tiempos de ejecución de `fn` para cada valor de `n_values`.
    """
    results = []
    for n in n_values:
        results.append(measure_time(fn, (n,)))
    return results

def plot_time_against_n(plt: plt, fn: callable, label: str):
    """
        Grafica los tiempos de ejecución de una función con los valores de `n`.

        :param plt: Objeto de matplotlib.pyplot.
        :type plt

        :param fn: Función a medir.
        :type callable

        :param label: Etiqueta para la serie de datos.
        :type str
    """
    times = measure_times_for(fn, N_VALUES)
    plt.plot(N_VALUES, times, label=label, color=np.random.rand(3,))
    plt.legend()

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Algoritmos según Notación Big O')

# O(1)
plot_time_against_n(plt, array_access_with, label='O(1) - Acceso de arreglo')

# O(log n)
plot_time_against_n(plt, binary_search_with, label='O(log n) - Búsqueda binaria')

# O(n)
plot_time_against_n(plt, linear_search_with, label='O(n) - Búsqueda lineal')

# O(n²)
plot_time_against_n(plt, bubble_sort_with, label='O(n²) - Ordenamiento burbuja')

# O(k^n)
plot_time_against_n(plt, fibonacci, label='O(k^n) - Serie de Fibonacci')

plt.show()
