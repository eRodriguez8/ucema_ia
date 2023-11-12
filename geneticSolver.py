from fitnessEvaluator import FitnessEvaluator
from populationGenerator import PopulationGenerator

class GeneticSolver:
    def __init__(self, population_size=100, mutation_rate=0.2, crossover_rate=0.8, max_generations=15000):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.max_generations = max_generations

    def solve(self, sudoku):
        # Inicializa las instancias de las clases necesarias
        fitness_evaluator = FitnessEvaluator()
        population_generator = PopulationGenerator(self.population_size)

        # Se copia el sudoku original
        current_solution = [[sudoku[row][col] for col in range(9)] for row in range(9)]

        # Genera una población inicial de soluciones. TOMA
        population = population_generator.random(current_solution)

        # Ejecuta el algoritmo genético
        for i in range(self.max_generations):
            for solution in population:
                fitness=fitness_evaluator.evaluate(solution)
                if fitness == 243:
                    print("Solución encontrada en la iteración", i + 1)
                    print()
                    return solution
           
            probabilities = self.calculateProbabilities(population, fitness_evaluator)

            population = population_generator.new(population, probabilities, sudoku, self.mutation_rate)
  
        # Retorna la mejor solución
        return max(population, key=fitness_evaluator.evaluate)

    def calculateProbabilities(self, population, fitness_function):
        fitnesses = [fitness_function.evaluate(solution) for solution in population]
        total_fitness = sum(fitnesses)
        return [fitness / total_fitness for fitness in fitnesses]


    #     # # Ejecuta el algoritmo genético
    #     for i in range(self.max_iterations):
    #         # Selecciona dos padres
    #         parent1, parent2 = self.selection(population, fitness_evaluator)

    #         # Cruza los padres con una cierta probabilidad
    #         if random.random() < self.crossover_rate:
    #             child1, child2 = crossover_operator.crossover(parent1, parent2)
    #         else:
    #             child1, child2 = parent1, parent2

    #         # Muta a los hijos con una cierta probabilidad
    #         if random.random() < self.mutation_rate:
    #             child1 = mutation_operator.mutate(child1, sudoku)
    #         if random.random() < self.mutation_rate:
    #             child2 = mutation_operator.mutate(child2, sudoku)

    #         # Evalúa la aptitud de los hijos
    #         fitness1 = fitness_evaluator.evaluate(child1)
    #         fitness2 = fitness_evaluator.evaluate(child2)

    #         # Sal del bucle si se alcanza una solución válida
    #         if fitness1 == 243 or fitness2 == 243:
    #             print("Solución encontrada en la iteración", i + 1)
    #             print()
    #             break

    #         # Reemplaza al padre más débil con el hijo más fuerte
    #         if fitness1 > fitness2:
    #             population.remove(parent1)
    #             population.append(child1)
    #         else:
    #             population.remove(parent2)
    #             population.append(child2)

    #     print("Maximas iteraciones alcanzadas")
    #     # Retorna la mejor solución
    #     return max(population, key=fitness_evaluator.evaluate)

    # @staticmethod
    # def selection(population, fitness_function):
    #         fitnesses = [fitness_function.evaluate(solution) for solution in population] #evalua cada fitness de las soluciones dentro de la poblacion.
    #         total_fitness = sum(fitnesses)  #suma el total de fitneses
    #         probabilities = [fitness / total_fitness for fitness in fitnesses]#probabilidades de cada solucion

    #         # Aumenta la probabilidad de seleccionar soluciones con una mayor aptitud
    #         parents = random.choices(population, probabilities, k=2)#selecciona a dos dentro de esas probabilidades
    #         return random.choice(parents), random.choice(parents)#de esos dos elige randoms, puede tocar el mismo.