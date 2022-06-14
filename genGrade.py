import typing
from grafo import grafo
from random import randint


def Grid(shape):
    n = shape[0] * shape[1]
    nodes = []
    for x in range(shape[0]):
        for y in range(shape[1]):
            if y == 0:
                if x != shape[0]-1:
                    neighbors = [(x + 1, y), (x, y + 1), (x + 1, y + 1)]
                else:
                    neighbors = [(x, y + 1)]
            elif y == shape[1]-1 and x != shape[0]-1:
                neighbors = [(x + 1, y), (x + 1, y - 1)]
            elif x == shape[0]-1:
                if y != shape[1]-1:
                    neighbors = [(x, y + 1)]
            else:
                neighbors = [(x + 1, y - 1), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            # print(x, ",", y, " ", neighbors)
            nodes.append(neighbors)

    tr = {}  # type: typing.Dict[tuple, list]
    cont = 0
    # Conta vertices
    for x in range(shape[0]):
        for y in range(shape[1]):
            # print((x, y), cont)
            tr[(x, y)] = cont
            cont += 1

    E = []
    c = 0
    for v in nodes:
        for u in v:
            # print(c, tr[u])
            if c != tr[u]:
                E.append((c, tr[u]))
        c += 1
    # print(E)
    # Gera o grafo
    g = grafo()
    V = [i for i in range(n)]
    for i in V:
        g.inserir_vertice(i)
    for e in E:
        a = randint(1, n)
        g.inserir_aresta(e[0], e[1], a)

    return [g, V, E]
