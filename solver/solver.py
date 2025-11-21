# solver.py
# -----------------------------------------------------------------------
# Módulo principal de resolución para Numberlink.
# Implementa backtracking + heurísticas.


import copy
from board.board import (
    set_cell,
    clear_cell,
    get_neighbors,
    is_inside,
)
from solver.validators import is_valid_move
from solver.heuristics import order_neighbors_by_priority
from model.pairs import order_pairs



def solve_board(T, P):
    """
    Resuelve el tablero Numberlink representado por la matriz T y la lista de parejas P.
    """

    # Ordenar según heurística (parejas más restrictivas primero)
    P_ordenadas = order_pairs(P, T)

    conectadas = []                 # parejas resueltas
    pendientes = P_ordenadas[:]     # copia

    return _resolver_parejas(T, P_ordenadas, 0, conectadas, pendientes)

#  Backtracking para parejas
def _resolver_parejas(T, P, indice, conectadas, pendientes):
    """
    Resuelve pareja por pareja según el orden P[indice].
    """

    # Caso base: todas resueltas
    if indice == len(P):
        return True

    pair = P[indice]
    (symbol, start, end) = pair

    T_backup = copy.deepcopy(T)
    C_i = [start]

    if _extender_camino(T, pair, C_i, conectadas, pendientes, P, indice):
        return True

    _restaurar_tablero(T, T_backup)
    return False


def _restaurar_tablero(T, T_backup):
    """
    Copia todo el contenido del backup en la matriz T.
    """
    N = len(T)
    M = len(T[0])
    for i in range(N):
        for j in range(M):
            T[i][j] = T_backup[i][j]

def _extender_camino(T, pair, C_i, conectadas, pendientes, P, indice_actual):
    """
    Intenta construir el camino C_i para conectar los extremos de la pareja.
    """

    (symbol, start, end) = pair
    c_actual = C_i[-1]

    # Si alcanzamos el objetivo → intentar siguiente pareja
    if _es_objetivo(c_actual, pair):
        conectadas.append(pair)
        if pair in pendientes:
            pendientes.remove(pair)

        # Resolver siguiente pareja
        if _resolver_parejas(T, P, indice_actual + 1, conectadas, pendientes):
            return True

        # Backtracking
        conectadas.remove(pair)
        pendientes.append(pair)
        return False

    # Evaluar vecinos
    (x, y) = c_actual
    vecinos = get_neighbors(x, y)
    vecinos = [(nx, ny) for (nx, ny) in vecinos if is_inside(T, nx, ny)]

    # Filtrar movimientos válidos
    candidatos = []
    for c_sig in vecinos:
        if is_valid_move(T, C_i, c_actual, c_sig, pair, pendientes):
            candidatos.append(c_sig)

    # Ordenar vecinos según heurísticas
    candidatos = order_neighbors_by_priority(candidatos, pair, T)

    # Intentar cada vecino
    for c_sig in candidatos:
        (nx, ny) = c_sig

        set_cell(T, nx, ny, symbol)
        C_i.append(c_sig)

        if _extender_camino(T, pair, C_i, conectadas, pendientes, P, indice_actual):
            return True

        # Si falla → Backtracking de esta celda
        C_i.pop()
        clear_cell(T, nx, ny)

    return False

def _es_objetivo(c_actual, pair):
    (_, _, end) = pair
    return c_actual == end
