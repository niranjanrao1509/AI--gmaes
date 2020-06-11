import argparse
from printBoard import printBoard
from Search import SearchStates
from hill_climbing import hill_climbing
from NQueens import NQueens

if __name__ == "__main__":
    n = 8
    itr = 10
    all_solns = 1
    test = SearchStates()
    problem = NQueens(n)
    result_states = test.Search(problem, hill_climbing, itr)
    printBoard(result_states, 0)
