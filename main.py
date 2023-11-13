from sudokus import Sudokus
from sudokuSolver import SudokuSolver
from sudokuPrinter import SudokuPrinter
from geneticSolver import GeneticSolver

population = 50
mutationRate = 0.2
generations = 500

sudokus = Sudokus()
solver = GeneticSolver(population, mutationRate, generations)
printer = SudokuPrinter()
sudokuSolver = SudokuSolver()
print()

easy = sudokus.easy()
medium = sudokus.medium()
hard = sudokus.hard()

printer.print_original(easy)
result = solver.solve(easy)
printer.print_resolved(result)