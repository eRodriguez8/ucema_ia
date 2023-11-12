import copy
import random
from mutationOperator import MutationOperator
from crossoverOperator import CrossoverOperator

class PopulationGenerator:
    def __init__(self, population_size):
        self.population_size = population_size
        self.mutation_operator = MutationOperator()
        self.crossover_operator = CrossoverOperator()

    def random(self, sudoku):
        population = [sudoku]
        for i in range(self.population_size - 1):
            solution = [[sudoku[row][col] for col in range(9)] for row in range(9)]
            for row in range(9):
                for col in range(9):
                    if solution[row][col] == 0:
                        solution[row][col] = random.randint(1, 9)
            population.append(solution)
        return population
    
    def new(self, population, probabilities, sudoku, mutation_rate, crossover_rate):
        children=[]

        for _ in range(self.population_size // 2):
            parents = random.choices(population, probabilities, k=2)
            parent1, parent2 = parents[0], parents[1]
            child1, child2 = self.crossover_operator.crossover(parent1, parent2)

            # Cruza los padres con una cierta probabilidad
            if random.random() < crossover_rate:
                child1, child2 = self.crossover_operator.crossover(parent1, parent2)
            else:
                child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)

            # Muta a los hijos con una cierta probabilidad
            if random.random() < mutation_rate:
                child1 = self.mutation_operator.mutate(child1, sudoku)
            if random.random() < mutation_rate:
                child2 = self.mutation_operator.mutate(child2, sudoku)
            
            children.append(child1)
            children.append(child2)
            
        return children