import random

#se generan v
class AvailableValues:
    @staticmethod
    def get(solution, sudoku):
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        while sudoku[row][col] != 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        # Encuentra los valores disponibles que no están en la fila, columna o bloque.
        available_values = list(set(range(1, 10)) - set(solution[row]) - set(solution[i][col] for i in range(9)) - set(solution[r][c] for r in range(row - row % 3, row - row % 3 + 3) for c in range(col - col % 3, col - col % 3 + 3)))

        return available_values, row, col