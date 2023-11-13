class FitnessEvaluator:
    @staticmethod
    def evaluate(solution):
        fitness = 0
        
        # Check rows
        # recorre cada fila, y suma los valores unicos. Cada fila sumaria 9, por ende sino hay nuemros repetidos esta iteracion sumaria 81
        for row in solution:
            fitness += len(set(row))
        
        # Check columns
        # recorre cada columna, y suma los valores unicos.  Cada columna sumaria 9, por ende sino hay nuemros repetidos esta iteracion sumaria 81 mas
        for col in range(9):
            column = [solution[row][col] for row in range(9)]
            fitness += len(set(column))
        
        # Check 3x3 boxes
        # recorre cada cuadrante, y suma los valores unicos. Cada cuadrante sumaria 9, por ende sino hay nuemros repetidos esta iteracion sumaria 81 mas
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = [solution[r][c] for r in range(row, row+3) for c in range(col, col+3)]
                fitness += len(set(box))
        
        # el fiteness devolveria 243 si no hay errores. 243 valores que no se repiten.   la suma de 81 + 81 + 81
        return fitness