import os

class SudokuPrinter:
    def print_sudoku(self, sudoku):
        print()
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("------+-------+------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(sudoku[i][j], end=" ")
            print()

    def print_original(self, sudoku):
        print("Sudoku Original")
        self.print_sudoku(sudoku)
        print()

    def print_resolved(self, sudoku):
        print("Sudoku Resolved")
        self.print_sudoku(sudoku)
        print()
