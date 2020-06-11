from random import choice


# METODO PARA IMPRESSAO DO TABULEIRO
def printBoard(result, param):
    if not result:
        print([None])
    if param == 0 and result:
        r = choice(result)
        board = []
        for col in r:
            line = ['.'] * len(r)
            line[col] = 'Q'
            board.append(str().join(line))

        charlist = map(list, board)
        for line in charlist:
            print (" ".join(line))
    else:
        board = []
        for r in result:
            for c in r:
                line = ['.'] * len(r)
                line[c] = 'Q'
                board.append(str().join(line))

        charlist = map(list, board)
        for i in range(0, len(list(charlist))):
            if i % len(charlist[i]) == 0:
                print("\n")

            print(" ".join(charlist[i]))
    print ("\n")
