import random

def solve_sudoku_genetic(sudoku):
    """
    This function takes a 9x9 sudoku grid as input and solves it using genetic algorithms.
    
    Parameters:
    sudoku (list): A 9x9 list representing the sudoku grid. Empty cells are represented by 0.
    
    Returns:
    list: A 9x9 list representing the solved sudoku grid.
    """
    # Define the fitness function
    def fitness_function(solution):
        fitness = 0
        
        # Check rows
        for row in solution:
            fitness += len(set(row))
        
        # Check columns
        for col in range(9):
            column = [solution[row][col] for row in range(9)]
            fitness += len(set(column))
        
        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = [solution[r][c] for r in range(row, row+3) for c in range(col, col+3)]
                fitness += len(set(box))
        
        return fitness
    
    # Define the genetic algorithm
    def genetic_algorithm(population, fitness_function):
        # Define the mutation function
        def mutation(solution):
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            # Find available values not in the row, column, or block
            available_values = list(set(range(1, 10)) - set(solution[row]) - set(solution[i][col] for i in range(9)) - set(solution[r][c] for r in range(row - row % 3, row - row % 3 + 3) for c in range(col - col % 3, col - col % 3 + 3)))

            if available_values:
                value = random.choice(available_values)
                solution[row][col] = value

            return solution
                
        # Define the crossover function
        def crossover(solution1, solution2):
            row = random.randint(0, 8)
            return solution1[:row] + solution2[row:], solution2[:row] + solution1[row:]
        
        # Define the selection function
        def selection(population, fitness_function):
            fitnesses = [fitness_function(solution) for solution in population]
            total_fitness = sum(fitnesses)
            probabilities = [fitness / total_fitness for fitness in fitnesses]

            # Increase the probability of selecting solutions with higher fitness
            parents = random.choices(population, probabilities, k=2)
            return random.choice(parents), random.choice(parents)
            
        # Run the genetic algorithm
        mutation_rate = 0.2  # Experimenta con diferentes tasas de mutación
        crossover_rate = 0.8  # Experimenta con diferentes tasas de cruce

        for i in range(5000):
            # Select two parents
            parent1, parent2 = selection(population, fitness_function)

            # Crossover the parents with a certain probability
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            # Mutate the children with a certain probability
            if random.random() < mutation_rate:
                child1 = mutation(child1)
            if random.random() < mutation_rate:
                child2 = mutation(child2)

            # Evaluate the fitness of the children
            fitness1 = fitness_function(child1)
            fitness2 = fitness_function(child2)

            # Print the fitness values for debugging
            # print(f"Iteration {i + 1}, Fitness 1: {fitness1}, Fitness 2: {fitness2}")

            # Salir del bucle si se alcanza una solución válida
            if fitness1 == 243 or fitness2 == 243:
                print("Solución encontrada en la iteración", i + 1)
                break

            if fitness1 > fitness2:
                population.remove(parent1)
                population.append(child1)
            else:
                population.remove(parent2)
                population.append(child2)

        # print("Final Population:")
        # for solution in population:
        #     print(fitness_function(solution), solution)

        # Return the best solution
        return max(population, key=fitness_function)
    
    # Convert the input sudoku to a list of lists
    sudoku = [[sudoku[row][col] for col in range(9)] for row in range(9)]
    
    # Generate an initial population of 100 solutions
    population = [sudoku]
    for i in range(99):
        solution = [[sudoku[row][col] for col in range(9)] for row in range(9)]
        for row in range(9):
            for col in range(9):
                if solution[row][col] == 0:
                    solution[row][col] = random.randint(1, 9)
        population.append(solution)
    
    # Solve the sudoku using genetic algorithms
    solution = genetic_algorithm(population, fitness_function)
    
    # Convert the solution back to a 9x9 list
    solution = [[solution[row][col] for col in range(9)] for row in range(9)]
    
    return solution

def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

sudoku_dificil = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_facil_multiple_soluciones = [
    [0, 2, 0, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 1, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]
]

# Imprimir el Sudoku incompleto
for fila in sudoku_facil_multiple_soluciones:
    print(fila)

matriz = solve_sudoku_genetic(sudoku_facil_multiple_soluciones)
print("matriz pelada")
print_sudoku(matriz)

print()

# def imprimir_matriz_booleana(matriz):
#     for fila in matriz:
#         print(" ".join(map(str, fila)))

# # Imprimir la matriz booleana
# print("Matriz Ocupada:")
# imprimir_matriz_booleana(matriz)

# import random
# from grafo import Grafo
# from dna import Dna

# #InICIALIZA VARIABLES

# #print("Ingrese cantidad de destinos: ")
# #num_nodos = int(input()) # Este es uno de los parámetros que vamos a poder modificar. Indicaría la cantidad de destinos que vamos a poner
# num_nodos=25

# #print("Ingrese cantidad de individuos: ")
# #cantidadPoblacion = int(input()) # Este es otro parámetro que vamos a poder modificar. Indica la cantidad de veces que se ejecuta el proceso de hacer una secuencia y ver el peso.
# cantidadPoblacion=10

# grafo = Grafo(num_nodos) # Se genera el grafo

# #PESOS ALEATORIOS a los nodos
# for i in range(num_nodos): # Se conectan los nodos. Ahora mismo asigné que los pesos sean entre 1 y 20 pero se puede variar a gusto.
#     for j in range(i + 1, num_nodos):
#         peso = random.randint(1, 20) # Se asignan los pesos y después se conectan.
#         grafo.conectar(i, j, peso)
    
# #CREAR POBLACION
# poblacion = []

# for i in range(0, cantidadPoblacion):
#     poblacion.append(Dna(grafo.num_nodos))

# # Muestran pesos -Obtener pesos
# for i in range(num_nodos): # Esta función va a imprimir el peso de cada conexión entre nodos.
#     for j in range(i + 1, num_nodos): # Se hace esto para que no se repitan las conexiones
#         peso = grafo.obtener_peso(i, j) # Se obtiene el peso
#         print(f'Peso entre Nodo {i} y Nodo {j}: {peso}') # Se imprime el peso.

# print()

# maxFitness = 0
# #calcular fitnes
# for individuo in poblacion:
#    individuo.getFitness(grafo)
    

# #SELECCION
# #aplicanod el metodo del dardo
# total_fitness=0
# for individuo in poblacion:
#    total_fitness=+individuo.fitness

# for individuo in poblacion:
#    individuo.prob_seleccion=(individuo.fitness/total_fitness)

# ruleta = [sum(individuo.prob_seleccion for individuo in poblacion[:i+1]) for i in range(len(poblacion))]

# seleccionados = []
# for _ in range(2):
#     numero_aleatorio = random.random()

#     # Buscar en qué sector de la ruleta cae el número aleatorio
#     for i, valor_acumulado in enumerate(ruleta):
#         if numero_aleatorio <= valor_acumulado:
#             seleccionados.append(poblacion[i])
#             break


# #seleccion
# print(seleccionados)

# #crosover

# #mutacion
# """


# primera_vuelta = 0 #esto es un flag que hace que la primera vez que se ejecuta el loop, se guarde el resultado como el más bajo, porque después va a haber una comparación.

# contador = 0
# optimo = 0


# for individuo in poblacion:
#     contador += 1
#     resultado = individuo.suma_pesos(grafo)
#     print(individuo.secuencia_nodos)
#     if primera_vuelta == 0:
#         masbajo = resultado
#         primera_vuelta = 1
#     print(f'Suma total de pesos en la secuencia aleatoria {contador}: {resultado}')
#     if resultado < masbajo: # si el resultado me dio menor a lo que guardé como más bajo, entonces es el nuevo más bajo
#         masbajo = resultado
#         optimo = contador

# print()
# print(f'El más bajo es: { masbajo } de la INDIVIDUO { optimo }')
# #poblacion = #esto hay que hacerlo
# #generacion = #esto hay que hacerlo

# #multi line comment
# """
# """
# Acá habría que hacer lo siguiente:
# - Generar una población inicial de secuencias aleatorias. La cantidad de individuos en la población va a indicar el número de veces que se repite el loop de abajo. Ahora mismo es "intentos".
# - Eso sería una generación.
# - Cuando termina esa generación hay que hacer el tema del fitness y la selección.
# - El fitness sería la suma de los pesos de la secuencia.
# - La selección sería elegir los mejores individuos de la población, y generar una nueva población con esos individuos. Crossover, mutación, todo eso.
# - Se hace la nueva generación, y se repite el proceso. Puede ser un for adentro de otro for¿?
# Ahí están los dos parámetros "población" y "generación" para ajustar esas cosas.
# """




# '''
# Ahora arranca esta parte que la hice provisoria. Es para ver cómo funciona el algoritmo de hacer una secuencia aleatoria y ver el peso.
# Básicamente es un bucle que se repite <intentos> veces. En cada iteración genera una secuencia aleatoria con todos los nodos, y suma los pesos de las conexiones.
# Se guarda en una variable el resultado más bajo y qué intento fue. Al final se imprimen esas dos cosas. 
# Acá habría que implementar lo genético.
# '''
# # inicializo variables




# '''
# Esto es lo que yo había puesto en la entrega anterior:
# '''


# # def distancia_entre_nodos(nodo1, nodo2):
# #
# # nodo_actual = 1
# # siguiente_nodo = 2
# #
# # def generar_random():
# #
# #
# # def Fitness(ruta):
# #     distancia_total = 0
# #     #para cada par de nodos consecutivos en la ruta:
# #     distancia_total += distancia_entre_nodos(nodo_actual, siguiente_nodo)
# #     return 1/distancia_total  # Se usa 1/d para minimizar en lugar de maximizar
# #
# # def Seleccion(poblacion, cantidad_de_padres):
# #     padres_seleccionados = []
# #
# #     suma_de_aptitudes = #se suman todas las aptitudes de los individuos
# #
# #     while len(padres_seleccionados) < cantidad_de_padres:
# #         numero_aleatorio = generar_random() #se genera un número aleatorio entre 0 y la suma de las aptitudes
# #         suma_acumulativa = 0.0
# #
# #         #se itera sobre la población hasta que la suma de las aptitudes sea mayor o igual al número aleatorio generado
# #         for individuo in poblacion:
# #             suma_acumulativa += individuo.aptitud #se suma la aptitud del individuo actual
# #
# #             # si la suma de las aptitudes es mayor o igual al número aleatorio generado, se agrega el individuo a la lista de padres seleccionados
# #             if suma_acumulativa >= numero_aleatorio:
# #                 padres_seleccionados.append(individuo)
# #                 break
# #
# #     return padres_seleccionados
# # padre1 = 1
# # padre2 = 2
# #
# # def crossover(padre1, padre2):
# #     '''
# #     1. Se genera aleatoriamente un punto de corte, entre 1 y la longitud del padre - 1
# #     2. Se copian los primeros nodos de padre1 hasta el punto de corte
# #     3. Para cada nodo en padre2 en el mismo orden:
# #     3.1 Si el nodo no está en el hijo:
# #     3.1.1 Se añade el nodo al hijo (así nos aseguramos de que no haya nodos repetidos)
# #     4. Se retorna el hijo
# #     '''
# #
# # numero_random = 1
# # posicion
# #
# #
# # def Mutacion(ruta, mutation_rate):
# #     if numero_random < mutation_rate:
# #         # Aplicar la mutación solo si un número aleatorio es menor que la tasa de mutación
# #         posicion_1 = # Seleccionar una posición aleatoria en la ruta
# #         posicion_2 = # Seleccionar otra posición aleatoria en la ruta
# #         ruta[posicion_1], ruta[posicion_2] = ruta[posicion_2], ruta[posicion_1] # Se intercambia el contenido de las posiciones seleccionadas