import random
from availableValues import AvailableValues

class MutationOperator:
    @staticmethod
    def mutate(solution, sudoku):
        available_values, row, col = AvailableValues.get(solution, sudoku)

        if available_values:
            value = random.choice(available_values)
            solution[row][col] = value

        return solution