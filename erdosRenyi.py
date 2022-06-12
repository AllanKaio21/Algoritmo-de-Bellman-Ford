from itertools import combinations
from random import randint, random
from grafo import grafo


def ER(n, p, direcionado=False):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = grafo(direcionado)
    for i in range(n):
        g.inserir_vertice(i)

    for e in E:
        if direcionado:
            a = randint(-10, n)
        else:
            a = randint(1, n)
        if a != 0:
            g.inserir_aresta(e[0], e[1], a)

    return [g, V, E]
