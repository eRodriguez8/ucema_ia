import random
from availableValues import AvailableValues

class MutationOperator:
    def mutate(self, solution, sudoku):
        for _ in range(3):  # Intenta realizar 3 mutaciones
            available_values, row, col = AvailableValues.get(solution, sudoku)

            if available_values:
                value = random.choice(available_values)
                solution[row][col] = value
                break

        return solution