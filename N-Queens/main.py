# MAIN CLASS
import argparse
from printBoard import printBoard
from Search import Search
from hill_climbing import hill_climbing
from hill_climbing import random_restart
from simulated_annealing import simulated_annealing
from NQueens import NQueensSearch

if __name__ == "__main__":
    n = 4
    itr = 10
    all_solns = 1
    test = Search()
    problem = NQueensSearch(n)
    problems = problem
    result_board = test.Search(problem, hill_climbing, itr)
    printBoard(result_board, args.all)
