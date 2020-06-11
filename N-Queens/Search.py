from time import time

class Search(object):
    def Search(self, problem, search_fn, i):
        n_iterations = i
        cnt = 0
        start = time()
        s = []
        for i in range(n_iterations):
            
            result = search_fn(problem)
            print("LOOP COUNT",i)
            print(result)
            print(problem.h_loss(result))
            if int(problem.h_loss(result)) is 0:
                print("RESULT IS 0")
                cnt += 1
                s.append(result)
        print (" - Hit rate: %2d/%d\tRuntime: %f" % (cnt, n_iterations, time() - start))
        return s
