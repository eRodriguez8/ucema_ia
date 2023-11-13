from sudokus import Sudokus
from sudokuSolver import SudokuSolver
from sudokuPrinter import SudokuPrinter
from geneticSolver import GeneticSolver

population = 50
mutationRate = 0.3
generations = 1000

sudokus = Sudokus()
solver = GeneticSolver(population, mutationRate, generations)
printer = SudokuPrinter()
sudokuSolver = SudokuSolver()
print()

easy = sudokus.easy()
medium = sudokus.medium()
hard = sudokus.hard()

printer.print_original(medium)
result = solver.solve(medium)
# result = sudokuSolver.solve_sudoku(medium)
printer.print_resolved(result)