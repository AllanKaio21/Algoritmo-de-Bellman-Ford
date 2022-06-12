from grafo import grafo
from bellmanFord import bellman_ford
from helpers import caminho_minino, plotGrafo, matrizAdjacencia, plotMatriz, plotCaminho, matrizDeCusto
from erdosRenyi import ER
import sys


class peso_negativo(Exception):
    pass


def main():
    # Cria um grado aleatorio usando Erdos Renyi
    g = ER(20, 0.5)
    # Plota o grafo
    # plotGrafo(g[1], g[2])

    # Matriz Adjacencia
    Madj = matrizAdjacencia(g[0])
    # Matriz de Custo
    Mcusto = matrizDeCusto(g[0])
    # params (grafo, V. origem, V. destino)
    todos = bellman_ford(g[0], 5)
    if(todos):
        for i in todos:
            print("Caminho: ", i[0], " Custo: ", i[1])
    else:
        print("Não existe caminho minimo!")

    print('------------------------------------------------------------')

    unico = bellman_ford(g[0], 5, 12)
    if (unico):
        for i in unico:
            print("Caminho: ", i[0], " Custo: ", i[1])
            # plotCaminho(g[1], g[2], i[0])
    else:
        print("Não existe caminho minimo!")

    # Plota as matrizes
    # plotMatriz(Madj, "Matriz de Adjacencia")
    # plotMatriz(Mcusto, "Matriz de Custo")


if __name__ == '__main__':
    main()
