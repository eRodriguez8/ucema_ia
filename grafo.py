from nodo import Nodo

class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos # acá se crean tantos nodos como pasamos como parámetro
        self.nodos = [Nodo(str(i)) for i in range(num_nodos)] # se crean los nodos, y se genera el nombre que es un número
        self.caminos_nodos = [[0] * num_nodos for _ in range(num_nodos)] # se crea la matriz de adyacencia, que es una matriz de ceros de tamaño num_nodos x num_nodos

    def conectar(self, nodo_origen, nodo_destino, peso): # se conectan los nodos, y se les asigna un peso
        if nodo_origen < self.num_nodos and nodo_destino < self.num_nodos: # si el nodo origen y el nodo destino son menores a la cantidad de nodos que tenemos
            self.caminos_nodos[nodo_origen][nodo_destino] = peso # se le asigna el peso a la matriz de adyacencia
            self.caminos_nodos[nodo_destino][nodo_origen] = peso

    def obtener_peso(self, nodo_origen, nodo_destino): # este método obtiene el peso de una conexión entre dos nodos
        if nodo_origen < self.num_nodos and nodo_destino < self.num_nodos: # si el nodo origen y el nodo destino son menores a la cantidad de nodos que tenemos
            return self.caminos_nodos[nodo_origen][nodo_destino] # entonces devolvemos el peso de la matriz de adyacencia
        return None
