import random
import copy

class CrossoverOperator:

    @staticmethod
    def crossover(solution1, solution2):
        row = random.randint(0, 8)
        
        # Usar deepcopy para realizar una copia profunda
        child1 = copy.deepcopy(solution1[:row] + solution2[row:])
        child2 = copy.deepcopy(solution2[:row] + solution1[row:])
        
        return child1, child2
    
    # def crossover(self, solution1, solution2):
    #     row = random.randint(0, 8)
        
    #     # Creamos copias para no modificar los padres originales
    #     child1 = [row.copy() for row in solution1]
    #     child2 = [row.copy() for row in solution2]

    #     # Intercambiamos solo las celdas con ceros entre los dos padres en la posición aleatoria
    #     for i in range(9):
    #         if solution1[row][i] == 0:
    #             child1[row][i], child2[row][i] = child2[row][i], child1[row][i]

    #     # Verificamos y corregimos si hay números duplicados en las filas
    #     child1 = self.ensure_unique_numbers(child1)
    #     child2 = self.ensure_unique_numbers(child2)

    #     return child1, child2

    # # Método para asegurarse de que cada número en la fila sea único
    # @staticmethod
    # def ensure_unique_numbers(solution):
    #     for row in solution:
    #         # Mientras haya duplicados en la fila, corregimos
    #         while any(row.count(num) > 1 for num in row):
    #             for i in range(9):
    #                 if row.count(row[i]) > 1:
    #                     row[i] = random.choice(list(set(range(1, 10)) - set(row)))
    #     return solution