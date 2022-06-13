from itertools import combinations
from random import randint, random
from grafo import grafo
from bellmanFord import bellman_ford


def ER(n, p, direcionado=False):
    # Codigo gerador de grafos aleatorios Erdos Renyi
    V = []
    while len(V) < n:
        a = randint(0, n - 1)
        if not a in V:
            V.append(a)

    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    # Cria um grafo e passa vertices e arestas gerados aleatorios
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

    # Retorna o grafo e suas vertices e arestas
    return [g, V, E]
