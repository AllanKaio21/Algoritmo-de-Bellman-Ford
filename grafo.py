from vertice import vertice


# Classe de criação de um grafo
class grafo:
    def __init__(self, direcionado=False):
        # Cria um array de vertices
        self._vertices = {}
        # Variavel de controle para grafos direcionados
        self.direcionado = direcionado

    def inserir_vertice(self, id):
        # Cria um vertice com o nome do parametro da função "id"
        v = vertice(id)
        # Insere na posição do nome a vertice criada
        self._vertices[id] = v
        # Retorna a vertice
        return v

    def inserir_aresta(self, de, para, peso=0):
        # Se a vertice principal não exite cria a vertice
        if de not in self._vertices:
            self.inserir_vertice(de)
        # Se a vertice a ser adicionada não existir, criar a vertice
        if para not in self._vertices:
            self.inserir_vertice(para)
        # Inserir a vertice principal a vertice adjacente
        self._vertices[de].inserir_vertice_adjacente(self._vertices[para], peso)
        # Se o grafo não for direcionado criar uma aresta de volta
        if not self.direcionado:
            self._vertices[para].inserir_vertice_adjacente(self._vertices[de], peso)

    def get_vertices(self):
        # Retorna todas as vertices
        return [v for k, v in self._vertices.items()]

    def get_vertice(self, id):
        # Verifica se a vertice existe : Se existir retorna suas informações Ex.: adjacentes, peso
        if id in self._vertices:
            return self._vertices[id]
        else:
            return None

    def get_arestas(self):
        # Cria um objeto : Vetor
        arestas = set()
        # Pega cada vertice
        for vertice in self._vertices.items():
            # Pega vertices adjacentes da "vertice"
            for a in vertice[1]._vertices_adjacentes:
                # Adiciona a vertice a aresta
                arestas.add((vertice[1], a))
        # Retorna as arestas do grafo
        return arestas

    def __iter__(self):
        return iter(self._vertices.values())
