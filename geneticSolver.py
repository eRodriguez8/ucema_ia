import random
from mutationOperator import MutationOperator
from fitnessEvaluator import FitnessEvaluator

class GeneticSolver:
    def __init__(self, population_size=100, mutation_rate=0.2, crossover_rate=0.8, max_iterations=5000):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.max_iterations = max_iterations

    def solve(self, sudoku):
        sudoku = [[sudoku[row][col] for col in range(9)] for row in range(9)]

        # Genera una población inicial de soluciones
        population = [sudoku]
        for i in range(self.population_size - 1):
            solution = [[sudoku[row][col] for col in range(9)] for row in range(9)]
            for row in range(9):
                for col in range(9):
                    if solution[row][col] == 0:
                        solution[row][col] = random.randint(1, 9)
            population.append(solution)

        # Inicializa las instancias de las clases necesarias
        fitness_evaluator = FitnessEvaluator()
        mutation_operator = MutationOperator()

        # Ejecuta el algoritmo genético
        for i in range(self.max_iterations):
            # Selecciona dos padres
            parent1, parent2 = self.selection(population, fitness_evaluator)

            # Cruza los padres con una cierta probabilidad
            if random.random() < self.crossover_rate:
                child1, child2 = self.crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            # Muta a los hijos con una cierta probabilidad
            if random.random() < self.mutation_rate:
                child1 = mutation_operator.mutate(child1)
            if random.random() < self.mutation_rate:
                child2 = mutation_operator.mutate(child2)

            # Evalúa la aptitud de los hijos
            fitness1 = fitness_evaluator.evaluate(child1)
            fitness2 = fitness_evaluator.evaluate(child2)

            # Sal del bucle si se alcanza una solución válida
            if fitness1 == 243 or fitness2 == 243:
                print("Solución encontrada en la iteración", i + 1)
                break

            # Reemplaza al padre más débil con el hijo más fuerte
            if fitness1 > fitness2:
                population.remove(parent1)
                population.append(child1)
            else:
                population.remove(parent2)
                population.append(child2)

        # Retorna la mejor solución
        return max(population, key=fitness_evaluator.evaluate)

    @staticmethod
    def selection(population, fitness_function):
            fitnesses = [fitness_function.evaluate(solution) for solution in population]
            total_fitness = sum(fitnesses)
            probabilities = [fitness / total_fitness for fitness in fitnesses]

            # Increase the probability of selecting solutions with higher fitness
            parents = random.choices(population, probabilities, k=2)
            return random.choice(parents), random.choice(parents)

    @staticmethod
    def crossover(solution1, solution2):
        row = random.randint(0, 8)
        return solution1[:row] + solution2[row:], solution2[:row] + solution1[row:]