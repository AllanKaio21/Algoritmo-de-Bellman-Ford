# Classe de criação de um vertice
class vertice:

    def __init__(self, id):
        # Define nome : id da vertice
        self._id = id
        # Cria um array de vertices adjacentes
        self._vertices_adjacentes = {}
        # Seta a distancia da vertice
        self._distancia = 0
        # Variavel auxiliar para controle de visitado
        self._visitado = False
        # Variavel auxiliar para anterior
        self._anterior = None

    def get_id(self):
        # Retorna nome : id da vertice
        return self._id

    def inserir_vertice_adjacente(self, para=None, peso=0):
        # Insere uma vertice adjacente
        self._vertices_adjacentes[para] = peso

    def get_vertices_adjacentes(self):
        # Retorna vertices adjacentes da vertice
        return self._vertices_adjacentes.keys()

    def get_distancia(self):
        # Retorna "distancia" da vertice
        return self._distancia

    def set_distancia(self, distancia):
        # Seta a "distancia" da vertice
        self._distancia = distancia

    def set_visitado(self):
        # Seta o estado "visitado" da vertice
        self._visitado = True

    def get_visitado(self):
        # Pega o estado "visitado" da vertice
        return self._visitado

    def get_peso(self, para):
        # Pega o peso da vertice
        return self._vertices_adjacentes[para]

    def set_anterior(self, anterior):
        # Seta o estado "anterior" da vertice
        self._anterior = anterior

    def get_anterior(self):
        # Pega o estado "anterior" da vertice
        return self._anterior

    def __str__(self):
        return str(self._id)
