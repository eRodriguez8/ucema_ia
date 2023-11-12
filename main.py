from sudokus import Sudokus
from sudokuSolver import SudokuSolver
from sudokuPrinter import SudokuPrinter
from geneticSolver import GeneticSolver

sudokus = Sudokus()
solver = GeneticSolver()
printer = SudokuPrinter()
sudokuSolver = SudokuSolver()
print()

easy = sudokus.easy()
medium = sudokus.medium()
hard = sudokus.hard()

print("Original")
printer.print(easy)
print()

result = solver.solve(easy)
# result = sudokuSolver.solve_sudoku(easy)

print("Resolved")
printer.print(result)
print()