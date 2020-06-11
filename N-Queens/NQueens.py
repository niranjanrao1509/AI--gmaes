# MODELAGEM DO PROBLEMA DE N-RAINHAS
from random import choice
from collections import Counter
from random import randrange


# Classe generica de problemas de busca
class SearchProblem:
    # Inicia a busca(recebe os parametros iniciais)
    def __init__(self, initial=None):
        pass

    # Define o estado inicial
    def initial(self):
        pass

    # Teste de objetivo
    def goal_test(self, state):
        pass

    # Heuristica, utilizada para problemas de maximizacao ou minimizacao
    def heuristic(self, state):
        pass

    # Retorna os estados acessiveis a partir do estado atual
    def nearStates(self, state):
        pass

    # Retorna uma escolha aleatoria dentre os estados proximos
    def randomNearState(self, state):
        return choice(self.nearStates(state))


# Implementacao do modelo do problema das n-rainhas, sobrescrevendo a classe SearchProblem
class NQueens(SearchProblem):
    
    def __init__(self, N):
        self.N = N

    def initial(self):
        return list(randrange(self.N) for i in range(self.N))

    def h_loss(self, state):
        a, b, c = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0  # inicia as colisoes com 0
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    def get_neighbours(self, state):
        neighbours = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  
                    neighbours.append(list(aux))  
        return neighbours
