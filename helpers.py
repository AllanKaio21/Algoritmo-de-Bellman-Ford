import matplotlib.pyplot as plt
import pandas as pd
import sys
from igraph import *
from grafo import grafo


def relax(u, v):
    if v.get_distancia() > u.get_distancia() + u.get_peso(v):
        v.set_distancia(u.get_distancia() + u.get_peso(v))
        v.set_anterior(u)


def initialize_single_source(g, s):
    # Passa por todas as vertices e seta a distancia como MAX
    for v in g.get_vertices():
        v.set_distancia(sys.maxsize)
    # Seta a distancia da vertice de origem como zero
    g.get_vertice(s).set_distancia(0)


def caminho_minino(v, caminho=None):
    # Verifica se o caminho esta nulo e seta com a vertice de origem
    if not caminho:
        caminho = [v.get_id()]
    # Se existir anterior insere no caminho
    if v._anterior:
        caminho.append(v.get_anterior().get_id())
        caminho_minino(v.get_anterior(), caminho)
    # Retorna o "caminho" invertido
    return caminho[::-1]


def plotGrafo(V, E):
    g = Graph()
    g.add_vertices(len(V))
    for i in E:
        g.add_edge(i[0], i[1])

    lista = g.get_edgelist()
    caminho = [2 for w in range(len(lista))]
    caminho_color = ["black" for i in range(len(lista))]

    g.es['weight'] = caminho
    visual_style = {"vertex_color": ["blue" for i in range(len(V))], "vertex_size": 20,
                    "vertex_label": [v for v in range(len(V))], "edge_width": g.es['weight'],
                    "edge_color": caminho_color, "bbox": (300, 300)}

    plot(g, **visual_style)


def plotCaminho(V, E, C):
    g = Graph()
    g.add_vertices(len(V))
    for i in E:
        g.add_edge(i[0], i[1])

    lista = g.get_edgelist()
    caminho = [2 for w in range(len(lista))]
    caminho_color = ["black" for i in range(len(lista))]
    for j in range(len(C) - 1):
        c = 0
        for i in range(len(lista)):
            if (lista[i][0] == C[j] and lista[i][1]) == C[j + 1] or (lista[i][1] == C[j] and lista[i][0] == C[j + 1]):
                caminho[c] = 5
                caminho_color[c] = "red"
            c = c + 1

    g.es['weight'] = caminho
    visual_style = {"vertex_color": ["blue" for i in range(len(V))], "vertex_size": 20,
                    "vertex_label": [v for v in range(len(V))], "edge_width": g.es['weight'],
                    "edge_color": caminho_color, "bbox": (300, 300)}

    plot(g, **visual_style)


def plotMatriz(M, nome="Matriz"):
    fig, ax = plt.subplots(1, 1)
    v = len(M)
    column_labels = [v for v in range(v)]
    row = column_labels
    df = pd.DataFrame(M, columns=column_labels)
    # colorR = ["red"]
    # colorC = ["blue"]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, rowLabels=row, cellLoc="center",
             loc='upper left')
    ax.set_title(nome,
                 fontweight="bold")

    plt.show()


def matrizAdjacencia(G):
    aux = len(G.get_vertices())
    matrizAdj = []
    for v in G.get_vertices():
        linha = [0 for v in range(aux)]
        for a in v.get_vertices_adjacentes():
            linha[a.get_id()] = 1
        matrizAdj.append(linha)

    return matrizAdj


def matrizDeCusto(G):
    aux = len(G.get_vertices())
    matrizCusto = []
    for v in G.get_vertices():
        linha = ["" for v in range(aux)]
        for a in v.get_vertices_adjacentes():
            linha[a.get_id()] = v.get_peso(a)

        matrizCusto.append(linha)

    return matrizCusto


def manual():
    dir = input("Grafo dirigido True / False? ")
    qtd = input("Quantidade de vertices: ")
    g = grafo(bool(dir))
    V = [i for i in range(int(qtd))]
    for i in range(int(qtd)):
        g.inserir_vertice(i)
    E = set()
    resp = 0
    while resp != 's':
        v = input("Vertice: ")
        a = input("Adjacente: ")
        E.add((v, a))
        p = input("Peso: ")
        g.inserir_aresta(int(v)-1, int(a)-1, float(p))

        resp = input("Digite 's' para sair 'c' para continuar: ")

    return [g, V, E]
