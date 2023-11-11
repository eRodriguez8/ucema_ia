import random

# Esta es la clase nodo, que representa un nodo en el grafo. El nombre es un número.
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre

class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos # acá se crean tantos nodos como pasamos como parámetro
        self.nodos = [Nodo(str(i)) for i in range(num_nodos)] # se crean los nodos, y se genera el nombre que es un número
        self.matriz_adyacencia = [[0] * num_nodos for _ in range(num_nodos)] # se crea la matriz de adyacencia, que es una matriz de ceros de tamaño num_nodos x num_nodos

    def conectar(self, nodo_origen, nodo_destino, peso): # se conectan los nodos, y se les asigna un peso
        if nodo_origen < self.num_nodos and nodo_destino < self.num_nodos: # si el nodo origen y el nodo destino son menores a la cantidad de nodos que tenemos
            self.matriz_adyacencia[nodo_origen][nodo_destino] = peso # se le asigna el peso a la matriz de adyacencia
            self.matriz_adyacencia[nodo_destino][nodo_origen] = peso

    def obtener_peso(self, nodo_origen, nodo_destino): # este método obtiene el peso de una conexión entre dos nodos
        if nodo_origen < self.num_nodos and nodo_destino < self.num_nodos: # si el nodo origen y el nodo destino son menores a la cantidad de nodos que tenemos
            return self.matriz_adyacencia[nodo_origen][nodo_destino] # entonces devolvemos el peso de la matriz de adyacencia
        return None


def suma_pesos_aleatoria(grafo): # este método suma los pesos de las conexiones de forma aleatoria. O sea, genera una secuencia de nodos al azar, y suma las conexiones.
    # Obtener una secuencia aleatoria de nodos
    secuencia_nodos = list(range(1, grafo.num_nodos))
    random.shuffle(secuencia_nodos)

    # Insertar el nodo inicial (nodo 0) al principio de la secuencia
    secuencia_nodos.insert(0, 0)

    print(secuencia_nodos) # Vemos la secuencia de nodos

    # Inicializar la suma total de pesos
    suma_total_pesos = 0

    # Recorrer la secuencia y sumar los pesos de las conexiones
    for i in range(len(secuencia_nodos) - 1):
        nodo_actual = secuencia_nodos[i]
        nodo_siguiente = secuencia_nodos[i + 1]

        peso = grafo.obtener_peso(nodo_actual, nodo_siguiente) # obtenemos el peso de la conexión entre el nodo actual y el nodo siguiente

        if peso is not None:
            suma_total_pesos += peso # sumamos el peso a la suma total de pesos, que se va acumulando en esa variable.

    # Sumar el peso de la última conexión
    peso_ultimo_nodo = grafo.obtener_peso(secuencia_nodos[-1], secuencia_nodos[0]) # hacemos que vuelve al origen, y sumamos el peso de esa conexión
    if peso_ultimo_nodo is not None:
        suma_total_pesos += peso_ultimo_nodo

    return suma_total_pesos


num_nodos = 5 # Este es uno de los parámetros que vamos a poder modificar. Indicaría la cantidad de destinos que vamos a poner
intentos = 4 # Este es otro parámetro que vamos a poder modificar. Indica la cantidad de veces que se ejecuta el proceso de hacer una secuencia y ver el peso.

#poblacion = #esto hay que hacerlo
#generacion = #esto hay que hacerlo

#multi line comment

"""
Acá habría que hacer lo siguiente:
- Generar una población inicial de secuencias aleatorias. La cantidad de individuos en la población va a indicar el número de veces que se repite el loop de abajo. Ahora mismo es "intentos".
- Eso sería una generación.
- Cuando termina esa generación hay que hacer el tema del fitness y la selección.
- El fitness sería la suma de los pesos de la secuencia.
- La selección sería elegir los mejores individuos de la población, y generar una nueva población con esos individuos. Crossover, mutación, todo eso.
- Se hace la nueva generación, y se repite el proceso. Puede ser un for adentro de otro for¿?
Ahí están los dos parámetros "población" y "generación" para ajustar esas cosas.
"""

grafo = Grafo(num_nodos) # Se genera el grafo

for i in range(num_nodos): # Se conectan los nodos. Ahora mismo asigné que los pesos sean entre 1 y 20 pero se puede variar a gusto.
    for j in range(i + 1, num_nodos):
        peso = random.randint(1, 20) # Se asignan los pesos y después se conectan.
        grafo.conectar(i, j, peso)

# Obtener pesos
for i in range(num_nodos): # Esta función va a imprimir el peso de cada conexión entre nodos.
    for j in range(i + 1, num_nodos): # Se hace esto para que no se repitan las conexiones
        peso = grafo.obtener_peso(i, j) # Se obtiene el peso
        print(f'Peso entre Nodo {i} y Nodo {j}: {peso}') # Se imprime el peso.


'''
Ahora arranca esta parte que la hice provisoria. Es para ver cómo funciona el algoritmo de hacer una secuencia aleatoria y ver el peso.
Básicamente es un bucle que se repite <intentos> veces. En cada iteración genera una secuencia aleatoria con todos los nodos, y suma los pesos de las conexiones.
Se guarda en una variable el resultado más bajo y qué intento fue. Al final se imprimen esas dos cosas. 
Acá habría que implementar lo genético.
'''
# inicializo variables
primera_vuelta = 0 #esto es un flag que hace que la primera vez que se ejecuta el loop, se guarde el resultado como el más bajo, porque después va a haber una comparación.
intento = 0

for i in range(intentos):
    resultado = suma_pesos_aleatoria(grafo)
    if primera_vuelta == 0:
        masbajo = resultado
        primera_vuelta = 1
    print(f'Suma total de pesos en la secuencia aleatoria {i}: {resultado}')
    if resultado < masbajo: # si el resultado me dio menor a lo que guardé como más bajo, entonces es el nuevo más bajo
        masbajo = resultado
        intento = i

print(f'El más bajo es: {masbajo} de la generación {intento + 1}')




'''
Esto es lo que yo había puesto en la entrega anterior:
'''


# def distancia_entre_nodos(nodo1, nodo2):
#
# nodo_actual = 1
# siguiente_nodo = 2
#
# def generar_random():
#
#
# def Fitness(ruta):
#     distancia_total = 0
#     #para cada par de nodos consecutivos en la ruta:
#     distancia_total += distancia_entre_nodos(nodo_actual, siguiente_nodo)
#     return 1/distancia_total  # Se usa 1/d para minimizar en lugar de maximizar
#
# def Seleccion(poblacion, cantidad_de_padres):
#     padres_seleccionados = []
#
#     suma_de_aptitudes = #se suman todas las aptitudes de los individuos
#
#     while len(padres_seleccionados) < cantidad_de_padres:
#         numero_aleatorio = generar_random() #se genera un número aleatorio entre 0 y la suma de las aptitudes
#         suma_acumulativa = 0.0
#
#         #se itera sobre la población hasta que la suma de las aptitudes sea mayor o igual al número aleatorio generado
#         for individuo in poblacion:
#             suma_acumulativa += individuo.aptitud #se suma la aptitud del individuo actual
#
#             # si la suma de las aptitudes es mayor o igual al número aleatorio generado, se agrega el individuo a la lista de padres seleccionados
#             if suma_acumulativa >= numero_aleatorio:
#                 padres_seleccionados.append(individuo)
#                 break
#
#     return padres_seleccionados
# padre1 = 1
# padre2 = 2
#
# def crossover(padre1, padre2):
#     '''
#     1. Se genera aleatoriamente un punto de corte, entre 1 y la longitud del padre - 1
#     2. Se copian los primeros nodos de padre1 hasta el punto de corte
#     3. Para cada nodo en padre2 en el mismo orden:
#     3.1 Si el nodo no está en el hijo:
#     3.1.1 Se añade el nodo al hijo (así nos aseguramos de que no haya nodos repetidos)
#     4. Se retorna el hijo
#     '''
#
# numero_random = 1
# posicion
#
#
# def Mutacion(ruta, mutation_rate):
#     if numero_random < mutation_rate:
#         # Aplicar la mutación solo si un número aleatorio es menor que la tasa de mutación
#         posicion_1 = # Seleccionar una posición aleatoria en la ruta
#         posicion_2 = # Seleccionar otra posición aleatoria en la ruta
#         ruta[posicion_1], ruta[posicion_2] = ruta[posicion_2], ruta[posicion_1] # Se intercambia el contenido de las posiciones seleccionadas