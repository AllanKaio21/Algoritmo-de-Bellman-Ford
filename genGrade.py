import typing
from grafo import grafo
from random import randint


def Grid(shape):
    n = shape[0] * shape[1]
    nodes = []
    # iterate through all combinations of coordinates
    for x in range(shape[0]):
        for y in range(shape[1]):
            # make and all possible neighbors
            if y == 0:
                print("1")
                if x != shape[0]-1:
                    neighbors = [(x + 1, y), (x, y + 1), (x + 1, y + 1)]
                else:
                    neighbors = [(x, y + 1)]
            elif y == shape[1]-1 and x != shape[0]-1:
                print("2")
                neighbors = [(x + 1, y), (x + 1, y - 1)]
            elif x == shape[0]-1:
                print("3")
                if y != shape[1]-1:
                    neighbors = [(x, y + 1)]
            else:
                print("4")
                neighbors = [(x + 1, y - 1), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            print(x, ",", y, " ", neighbors)
            nodes.append(neighbors)

    tr = {}  # type: typing.Dict[tuple, list]
    cont = 0

    for x in range(shape[0]):
        for y in range(shape[1]):
            tr[(x, y)] = cont
            cont += 1
    E = set()
    c = 0
    for v in nodes:
        for u in v:
            E.add((c, tr[u]))
        c += 1

    g = grafo()
    V = [i for i in range(n)]
    for i in V:
        g.inserir_vertice(i)
    for e in E:
        a = randint(1, n)
        g.inserir_aresta(e[0], e[1], a)

    return [g, V, E]
