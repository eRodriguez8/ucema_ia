class SudokuSolver:
    def solve_sudoku(self, board):
        # Encuentra una celda vacía
        empty = self.find_empty(board)
        
        # Si no hay celdas vacías, el sudoku está resuelto
        if not empty:
            return True
        
        row, col = empty
        
        # Intenta colocar un número del 1 al 9 en la celda vacía
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                # Si el número es válido, colócalo y sigue resolviendo
                board[row][col] = num
                
                if self.solve_sudoku(board):
                    return board  # Sudoku resuelto
                
                # Si la colocación no lleva a una solución, retrocede
                board[row][col] = 0
        
        # No se encontró ninguna solución para esta configuración
        return False
    
    @staticmethod
    def find_empty(board):
        # Encuentra la primera celda vacía en el tablero
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    @staticmethod
    def is_valid(board, num, pos):
        # Verifica si es seguro colocar 'num' en la posición 'pos'
        
        # Verifica la fila
        if num in board[pos[0]]:
            return False
        
        # Verifica la columna
        if num in [board[i][pos[1]] for i in range(9)]:
            return False
        
        # Verifica el cuadrante 3x3
        box_row, box_col = pos[0] // 3 * 3, pos[1] // 3 * 3
        if num in [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]:
            return False
        
        return True