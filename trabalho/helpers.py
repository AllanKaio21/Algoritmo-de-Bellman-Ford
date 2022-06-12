import sys


def relax(u, v):
    if v.get_distancia() > u.get_distancia() + u.get_peso(v):
        v.set_distancia(u.get_distancia() + u.get_peso(v))
        v.set_anterior(u)


def initialize_single_source(g, s):
    for v in g.get_vertices():
         v.set_distancia(sys.maxsize)

    g.get_vertice(s).set_distancia(0)

def caminho_minino(v, caminho):
    if v._anterior:
        caminho.append(v.get_anterior().get_id())
        caminho_minino(v.get_anterior(), caminho)
    return