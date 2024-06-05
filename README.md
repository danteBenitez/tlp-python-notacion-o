# Notación Big O: Actividad de investigación

## Ejemplos de algoritmos por complejidad

### Algoritmo de complejidad constante O(1)

#### Acceso a índice de un arreglo 

Debido a que los elementos de un arreglo se almacenan en posiciones de memoria contiguas, el acceso a un elemento en una posición específica se realiza en tiempo constante. Por ello, la posición de memoria de un elemento con índice n, puede calcularse como:
    
    ```
    dirección de memoria = dirección base + (tamaño de elemento) * n
    ```

Donde la dirección base es la dirección de memoria del primer elemento del arreglo y el tamaño de elemento es la cantidad de bytes que ocupa un elemento del arreglo. Las listas de Python son un ejemplo de estructura de datos que se almacenan en memoria de forma contigua, si bien no son arreglos en el sentido tradicional (son vectores dinámicos).

Dado que el acceso a un índice de un arreglo no depende de la cantidad de elementos que contiene, la complejidad de este algoritmo es O(1).

### Algoritmo de complejidad logarítmica O(log n)

#### Búsqueda binaria

Este algoritmo es de complejidad logarítmica porque la cantidad de pasos que se realiza es proporcional al logaritmo de la cantidad de elementos que se recorren. En el caso de la búsqueda binaria, dado que se divide el arreglo en dos partes por iteración, la cantidad de pasos que realiza se puede calcular con el logaritmo base 2 del número de elementos.

### Algoritmo de complejidad lineal O(n)

#### Búsqueda lineal

Este algoritmo es de complejidad lineal porque la cantidad de pasos que se realiza es proporcional a la cantidad de elementos que se recorren. Para un arreglo de n elementos, en el peor de los casos, se realizan n pasos con una duración constante (en este caso, el paso es la comprobación de que un elemento sea el buscado). 

### Algoritmo de complejidad log lineal O(n * log n)

#### Quick sort

Este algoritmo es de complejidad log lineal porque la cantidad de pasos que se realiza es proporcional al producto de la cantidad de elementos que se recorren y el logaritmo de la cantidad de elementos que se recorren. En Quick sort, un arreglo se subdivide en dos arreglos y se ordenan de forma recursiva. Si bien la complejidad concreta depende de la elección del elemento pivote, el caso promedio tiene una complejidad de O(n * log n).

### Algoritmo de complejidad cuadrática O(n^2)

#### Ordenamiento burbuja

Este algoritmo es de complejidad cuadrática porque la cantidad de pasos que se realiza es proporcional al cuadrado de la cantidad de elementos que se recorren. El ordenamiento burbuja realiza un bucle anidado, realiza comparaciones en cada iteración de un elemento con su siguiente y, si no están ordenados, los intercambia. 

### Algoritmo de complejidad exponencial O(k^n)

#### Sucesión de Fibonacci recursiva

Este algoritmo es de complejidad exponencial porque la cantidad de pasos que se realiza es proporcional a 2 elevado a la cantidad de elementos que se recorren. Para calcular el enésimo número  de la sucesión Fibonacci con esta técnica, necesitamos calcular el número n-1 y el número n-2, y así sucesivamente. Dado que cada número se calcula a partir de dos números anteriores, la cantidad de pasos que se realiza es exponencial. Concretamente, la base del exponente es k = φ, que es el número áureo, con un valor aproximado de 1.61803398875.

## Sobre el proyecto


