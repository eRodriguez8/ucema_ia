import random

class MutationOperator:
    @staticmethod
    def mutate(solution):
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        # Find available values not in the row, column, or block
        available_values = list(set(range(1, 10)) - set(solution[row]) - set(solution[i][col] for i in range(9)) - set(solution[r][c] for r in range(row - row % 3, row - row % 3 + 3) for c in range(col - col % 3, col - col % 3 + 3)))

        if available_values:
            value = random.choice(available_values)
            solution[row][col] = value

        return solution