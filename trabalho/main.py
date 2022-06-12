from grafo import grafo
from bff import bellman_ford
from helpers import caminho_minino


class peso_negativo(Exception):
    pass


def main():
    g = grafo(direcionado=True)

    g.inserir_vertice('A')
    g.inserir_vertice('B')
    g.inserir_vertice('C')
    g.inserir_vertice('D')
    g.inserir_vertice('E')

    g.inserir_aresta('A', 'B', 6)
    g.inserir_aresta('A', 'C', 7)
    g.inserir_aresta('A', 'E', 2)
    g.inserir_aresta('B', 'D', 5)
    g.inserir_aresta('B', 'C', 8)
    g.inserir_aresta('B', 'E', -4)
    g.inserir_aresta('C', 'D', -3)
    g.inserir_aresta('C', 'E', 9)
    g.inserir_aresta('D', 'B', -2)
    g.inserir_aresta('E', 'D', 7)

    bellman_ford(g, 'D')

    for v in g.get_vertices():
        caminho = [v.get_id()]
        caminho_minino(v, caminho)
        print('O menor caminho é: %s com custo %d.' %(caminho[::-1], v.get_distancia()))


if __name__ == '__main__':
    main()
