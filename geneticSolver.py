from fitnessEvaluator import FitnessEvaluator
from populationGenerator import PopulationGenerator

class GeneticSolver:
    def __init__(self, population_size=100, mutation_rate=0.3, max_generations=1000):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations

    def solve(self, sudoku):
        # Inicializa las instancias de las clases necesarias
        fitness = 0
        fitness_evaluator = FitnessEvaluator()
        population_generator = PopulationGenerator(self.population_size)

        # Se copia el sudoku original
        current_solution = [[sudoku[row][col] for col in range(9)] for row in range(9)]

        # Genera una población inicial de soluciones.
        population = population_generator.random(current_solution)

        # Ejecuta el algoritmo genético
        for i in range(self.max_generations):
            for solution in population:
                fitness = fitness_evaluator.evaluate(solution)
                print("Fitness actual: " + str(fitness))
                if fitness == 243:
                    print()
                    print("Solución encontrada en la generacion", i + 1)
                    print()
                    return solution
           
            probabilities = self.calculate_probabilities(population, fitness_evaluator)
            
            population = population_generator.new(population, probabilities, sudoku, self.mutation_rate)
  
        # Retorna la mejor solución
        print()
        print("Fitness final: " + str(fitness))
        print()
        return max(population, key=fitness_evaluator.evaluate)

    def calculate_probabilities(self, population, fitness_function):
        fitnesses = [fitness_function.evaluate(solution) for solution in population]
        total_fitness = sum(fitnesses)
        return [fitness / total_fitness for fitness in fitnesses]