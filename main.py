from bellmanFord import bellman_ford
from helpers import *
from erdosRenyi import ER
from genGrade import Grid
from grafo import grafo


def main():

    g = Grid((6, 6))

    plotGrafo(g[1], g[2])

    # g = None
    # print("Selecione uma Opção: ")
    # print("1 - Inserir grafo manualmente ")
    # print("2 - Gerar grafo aleatorio")
    # print("3 - Sair")
    # a = input("=> ")
    #
    # if a == '1':
    #     g = manual()
    # elif a == '2':
    #     v = input("Digite quantidade de vertices: ")
    #     p = input("Digite probabilidade: ")
    #     d = input("Digite se é dirigidor True / False: ")
    #     g = ER(int(v), float(p), bool(d))
    # else:
    #     print("Bye!")
    #     return 1
    #
    # o = input("Escolha vertice de origem: ")
    # d = input("Escolha vertice de destino: ")
    # res = bellman_ford(g[0], int(o), int(d))
    # if res:
    #     for i in res:
    #         print("Caminho: ", i[0], " Custo: ", i[1])
    #         plotCaminho(g[1], g[2], i[0])
    # else:
    #     print("Não existe caminho minimo!")
    #
    # # Plota o grafo
    # plotGrafo(g[1], g[2])
    #
    # # Matriz Adjacencia
    # Madj = matrizAdjacencia(g[0])
    #
    # # Matriz de Custo2
    #
    # Mcusto = matrizDeCusto(g[0])
    #
    # # Plota as matrizes
    # plotMatriz(Madj, "Matriz de Adjacencia")
    # plotMatriz(Mcusto, "Matriz de Custo")


if __name__ == '__main__':
    main()
