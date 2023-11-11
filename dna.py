import random

class Dna:
    def __init__(self, num_nodos):
        self.dnaLength = num_nodos
        self.fitness=0
        prob_seleccion=0

        # Genes
        self.secuencia_nodos = list(range(1, self.dnaLength))
        random.shuffle(self.secuencia_nodos)

        # Insertar el nodo inicial (nodo 0) al principio de la secuencia
        self.secuencia_nodos.insert(0, 0)
        print('Secuencia individuo: ') # Vemos la secuencia de nodos
        print(self.secuencia_nodos)


#este es el claulo de fitness
    def getFitness(self, grafo): # este método suma los pesos de las conexiones de forma aleatoria. O sea, genera una secuencia de nodos al azar, y suma las conexiones.
        # Inicializar la suma total de pesos
        suma_total_pesos = 0

        # Recorrer la secuencia y sumar los pesos de las conexiones
        for i in range(len(self.secuencia_nodos) - 1):
            nodo_actual = self.secuencia_nodos[i]
            nodo_siguiente = self.secuencia_nodos[i + 1]

            peso = grafo.obtener_peso(nodo_actual, nodo_siguiente) # obtenemos el peso de la conexión entre el nodo actual y el nodo siguiente

            if peso is not None:
                suma_total_pesos += peso # sumamos el peso a la suma total de pesos, que se va acumulando en esa variable.

        # Sumar el peso de la última conexión
        peso_ultimo_nodo = grafo.obtener_peso(self.secuencia_nodos[-1], self.secuencia_nodos[0]) # hacemos que vuelve al origen, y sumamos el peso de esa conexión
        if peso_ultimo_nodo is not None:
            suma_total_pesos += peso_ultimo_nodo
      
        self.fitness = 1/suma_total_pesos
        return self.fitness

