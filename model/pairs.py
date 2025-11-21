# pairs.py
# -----------------------------------------------------------------------
# Detección y manejo de parejas p_i a partir de la matriz T.


from board.board import get_neighbors, is_inside


def extract_pairs(T):
    """
    Recorre la matriz T para identificar todos los símbolos que aparecen
    exactamente dos veces y construye la lista de parejas P.
    """

    coordenadas = {} 

    N = len(T)
    M = len(T[0])

    # Recorrido de izquierda a derecha y de arriba hacia abajo
    for x in range(N):
        for y in range(M):
            celda = T[x][y]

            # Ignorar celdas vacías
            if celda == ".":
                continue

            if celda not in coordenadas:
                coordenadas[celda] = []
            coordenadas[celda].append((x, y))

    # Construir lista de parejas P
    P = []

    for simbolo, coords in coordenadas.items():
        if len(coords) != 2:
            raise ValueError(
                f"El símbolo '{simbolo}' aparece {len(coords)} veces, "
                f"pero debería aparecer exactamente 2."
            )

        (x1, y1), (x2, y2) = coords
        p_i = (simbolo, (x1, y1), (x2, y2))
        P.append(p_i)

    return P


# -------- Heurística para ordenar parejas (más difíciles primero) --------

def _manhattan(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    return abs(x1 - x2) + abs(y1 - y2)


def _count_free_neighbors(T, celda):
    (x, y) = celda
    count = 0
    for nx, ny in get_neighbors(x, y):
        if is_inside(T, nx, ny) and T[nx][ny] == ".":
            count += 1
    return count


def pair_difficulty(pair, T):
    """
    Calcula una medida de 'dificultad' de la pareja.
    """
    (symbol, start, end) = pair
    dist = _manhattan(start, end)

    espacio = _count_free_neighbors(T, start) + _count_free_neighbors(T, end)

    # Puedes ajustar esta fórmula si luego quieres refinarla
    dificultad = dist * 2 + (4 - espacio)
    return dificultad


def order_pairs(P, T):
    """
    Ordena la lista de parejas P aplicando la heurística de dificultad:
    las parejas más restrictivas/difíciles primero.
    """
    return sorted(P, key=lambda p: pair_difficulty(p, T))
