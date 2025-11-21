# heuristics.py
# -----------------------------------------------------------------------
# Heurísticas utilizadas para priorizar parejas y movimientos en Numberlink.

from board.board import get_neighbors, is_inside
import math

# Distancia Manhattan
def manhattan(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    return abs(x1 - x2) + abs(y1 - y2)


# Heurística: parejas más restringidas primero
def pair_difficulty(pair, T):
    """
    Calcula una medida de 'dificultad' de la pareja.
    """
    (symbol, start, end) = pair
    (xs, ys) = start
    (xf, yf) = end
    # Distancia entre extremos
    dist = manhattan(start, end)
    # Celdas vacías alrededor de cada extremo
    def count_free_neighbors(celda):
        (x, y) = celda
        count = 0
        for nx, ny in get_neighbors(x, y):
            if is_inside(T, nx, ny) and T[nx][ny] == ".":
                count += 1
        return count
    espacio = count_free_neighbors(start) + count_free_neighbors(end)
    dificultad = dist * 2 + (4 - espacio)
    return dificultad


def order_pairs(P, T):
    """
    Ordena las parejas según la dificultad estimada.
    """
    return sorted(P, key=lambda p: pair_difficulty(p, T))

def branching_factor(T, cell):
    """
    Cuenta cuántas extensiones posibles tiene la celda.
    """
    (x, y) = cell
    posibles = 0
    for nx, ny in get_neighbors(x, y):
        if is_inside(T, nx, ny) and T[nx][ny] == ".":
            posibles += 1
    return posibles


def order_neighbors_by_priority(neighbors, pair, T):
    """
    Ordena las celdas vecinas según heurísticas
    """
    (_, _, end) = pair
    def score(c):
        # Criterio 1: distancia al destino
        d = manhattan(c, end)
        # Criterio 2: menor branching factor = mejor
        b = branching_factor(T, c)
        # Criterio 3: celdas libres alrededor (para mantener flexibilidad)
        free = sum(
            1 for nx, ny in get_neighbors(c[0], c[1])
            if is_inside(T, nx, ny) and T[nx][ny] == "."
        )
        # devolver una tupla ordenable (priorizar d, luego b, luego -free)
        return (d, b, -free)
    return sorted(neighbors, key=score)
