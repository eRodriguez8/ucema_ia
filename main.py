from sudokuPrinter import SudokuPrinter
from geneticSolver import GeneticSolver
from sudokus import Sudokus

sudokus = Sudokus()
solver = GeneticSolver(100, 0.3, 0.8, 5000)
printer = SudokuPrinter()

reallyEasy = sudokus.reallyEasy()
easy = sudokus.easy()
medium = sudokus.medium()
hard = sudokus.hard()

print("Sudoku muy facil: ")
printer.print(reallyEasy)
print()

result = solver.solve(reallyEasy)

print("Sudoku muy facil resuelto: ")
printer.print(result)
print()

# print("Sudoku facil: ")
# printer.print(easy)
# print()

# result = solver.solve(easy)

# print("Sudoku facil resuelto: ")
# printer.print(result)
# print()

# print("Sudoku medio: ")
# printer.print(medium)
# print()

# result = solver.solve(medium)

# print("Sudoku medio resuelto: ")
# printer.print(result)
# print()

# print("Sudoku dificil: ")
# printer.print(hard)
# print()

# result = solver.solve(hard)

# print("Sudoku dificil resuelto: ")
# printer.print(result)
# print()
