class FitnessEvaluator:
    @staticmethod
    def evaluate(solution):
        fitness = 0
        
        # Check rows
        for row in solution:
            fitness += len(set(row))
        
        # Check columns
        for col in range(9):
            column = [solution[row][col] for row in range(9)]
            fitness += len(set(column))
        
        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = [solution[r][c] for r in range(row, row+3) for c in range(col, col+3)]
                fitness += len(set(box))
        
        return fitness