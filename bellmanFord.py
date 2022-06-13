from helpers import relax, initialize_single_source, caminho_minino
import sys


def bellman_ford(g, s, c=None):
    # Inicializa a distancia das vertices como MAXSIZE
    initialize_single_source(g, s)
    # Percorre todas as vertices
    for k in g.get_vertices():
        # Pega areta do grafo
        for u, v in g.get_arestas():
            # Verifica se aresta foi visitada : Se sim continua
            if v.get_visitado():
                continue
            # Atualiza as distancias das vertices
            relax(u, v)
    # Pega aresta
    for u, v in g.get_arestas():
        if v.get_distancia() > u.get_distancia() + u.get_peso(v):
            print("O grafo contem ciclos negativos!")
            return False
    caminho = []
    for v in g.get_vertices():
        if v.get_id() == c or c == None:
            if v.get_distancia() != sys.maxsize:
                caminho.append([caminho_minino(v), v.get_distancia()])

    # Se não existir caminho minimo
    if not caminho:
        return False
    # Retorna um vetor com [[Caminho minimo, Distancia]]
    return caminho
