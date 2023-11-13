import copy
import random

class CrossoverOperator:
    @staticmethod
    def crossover(solution1, solution2):
        row = random.randint(0, 8)

        child1 = copy.deepcopy(solution1[:row] + solution2[row:])
        child2 = copy.deepcopy(solution2[:row] + solution1[row:])
        
        return child1, child2