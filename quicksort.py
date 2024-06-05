# Extraído de https://github.com/danteBenitez/tlp-python-quicksort/blob/main/quicksort.py

def quicksort(number_list: list[int | float]) -> list[int | float]:
    """
        Utiliza el algoritmo de quicksort para ordenar una lista de números
        *in_place* (sin utilizar memoria adicional).

        :param number_list: lista de números a ordenar
        :type list[int | float]

        :return: lista de números ordenados
        :rtype: list[int | float]
    """
    # Aquí llamamos a la implementación de quicksort.
    # Lo realizamos de este modo para que consumidores de la función 
    # no deban preocuparse por colocar los índices correctos.
    return quicksort_impl(number_list, 0, len(number_list) - 1)

def quicksort_impl(number_list: list[int | float], start: int, end: int) -> list[int | float]:
    """
        Implementación recursiva del algoritmo de quicksort
        que ordena una sublista de `number_list` dado un rango
        de índices [start, end). El ordenamiento es *in_place*.

        :param number_list: lista de números a ordenar
        :type list[int | float]

        :param start: índice de inicio de la sublista
        :type int

        :param end: índice de fin de la sublista
        :type int
    """
    # El largo de la sublista. Puesto que los límites son inclusivos, 
    # sumamos uno para obtener el largo real.
    length = end - start + 1
    # Caso base:
    # Si el largo es menor o igual a 1, entonces la sublista ya está ordenada.
    # Retornar la lista como está.
    if length <= 1:
        return number_list

    # Selección del pivote como el elemento medio de la sublista.
    pivot_index = start + (end - start) // 2
    pivot = number_list[pivot_index]

    # Partición: Reordenamos la sublista de modo que los valores menores al 
    # pivote se encuentren a la izquierda y los mayores a la derecha de un índice
    # dado por `pivot_index`. Lo que sigue es una implementación de la partición 
    # de Hoare, que tiene mejor complejidad algoritmica que sus alternativas.
    # Véase: https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme

    # Definimos dos índices, uno izquierdo y otro derecho.
    left = start - 1
    right = end + 1
    while True:
        # Avanzamos el índice izquierdo mientras encontremos valores
        # menores que el pivote.
        left += 1
        while number_list[left] < pivot:
            left += 1

        # Avanzamos el índice derecho mientras encontremos valores
        # mayores que el pivote. 
        right -= 1
        while number_list[right] > pivot:
            right -= 1

        # Si los índices se han cruzado, entonces el algoritmo ha terminado.
        if left >= right:
            # Para este punto, las siguientes condiciones se cumplen:
                # - a la derecha del índice `right` hay valores no menores al pivote
                #   (puesto que los que eran menores se han intercambiado)
                # - a la izquierda del índice `right` hay valores no mayores al pivote
                #    (puesto que los que eran mayores se han intercambiado)
            # Es decir, el índice `right` cumple con las condiciones de la partición
            # y podemos usarlo para continuar con el ordenamiento.
            pivot_index = right
            break
        
        # Si no, intercambiamos las posiciones de los elementos correspondientes.
        number_list[left], number_list[right] = number_list[right], number_list[left]

    # Caso recursivo: Llamamos a *quicksort_impl* para ordenar
    # las sublistas que formamos: 
        # - una sublista va desde start hasta pivot_index
        # - la otra va desde pivot_index + 1 hasta end
    quicksort_impl(number_list, start, pivot_index)
    quicksort_impl(number_list, pivot_index + 1, end)

    # Finalizamos la recursión retornando la lista luego de que haya sido
    # modificado por las anteriores llamadas
    return number_list