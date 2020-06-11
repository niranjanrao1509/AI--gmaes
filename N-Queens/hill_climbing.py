from random import shuffle

def hill_climbing(problem):
    current = problem.initial()
    while True:
        neighbours = problem.get_neighbours(current)
        print("heyyy")
        if not neighbours:
            break
        neighbour = max(neighbours, key=lambda state: problem.h_loss(state))
        if problem.h_loss(neighbour) <= problem.h_loss(current):
            break
        current = neighbour
    return current

def random_restart(problem, limit=10):
    state = problem.initial()
    count = 0
    while problem.goal_test(state) == False and count < limit:
        state = hill_climbing(problem)
        count += 1
    return state
