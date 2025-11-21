# validators.py
# -----------------------------------------------------------------------
# Validaciones para extender un camino:
# 1. Adyacencia ortogonal
# 2. Celda dentro del tablero
# 3. Celda vacía o destino de la misma pareja
# 4. Camino simple (no repetir celdas)
# 5. No cruzar caminos de otras parejas
# 6. Mantener alcanzabilidad del destino
# -----------------------------------------------------------------------

from collections import deque
from board.board import is_inside, is_empty, get_cell, get_neighbors

# 1. Adyacencia ortogonal
def is_adjacent(c_actual, c_sig):
    (x, y) = c_actual
    (nx, ny) = c_sig
    return abs(x - nx) + abs(y - ny) == 1

# 2. Celda dentro del tablero
def inside_board(T, c_sig):
    x, y = c_sig
    return is_inside(T, x, y)

# 3. Celda vacía o destino final de la misma pareja
def cell_free_or_target(T, c_sig, pair):
    (symbol, start, end) = pair
    (x2, y2) = end
    (x, y) = c_sig

    # si es el destino final, la celda siempre es válida
    if (x, y) == (x2, y2):
        return True

    # en otro caso debe ser una celda vacía
    return is_empty(T, x, y)

# 4. Camino simple: no repetir celdas
def not_in_path(C_i, c_sig):
    return c_sig not in C_i

# 5. No cruzar caminos de otras parejas
def not_other_pair_path(T, c_sig, pair):
    (symbol, start, end) = pair
    (x, y) = c_sig

    celda = get_cell(T, x, y)

    if celda == symbol:
        return (x, y) == end

    # si la celda contiene algún otro símbolo → no válido
    if celda != ".":
        return False

    return True

# 6. Alcanzabilidad del destino
def reachable(T, c_sig, pair):
    (symbol, start, end) = pair
    (xf, yf) = end

    queue = deque([c_sig])
    visited = {c_sig}

    N, M = len(T), len(T[0])

    while queue:
        x, y = queue.popleft()

        if (x, y) == (xf, yf):
            return True

        for nx, ny in get_neighbors(x, y):
            if 0 <= nx < N and 0 <= ny < M:

                if (nx, ny) not in visited:
                    if T[nx][ny] == "." or (nx, ny) == (xf, yf):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

    return False

# Validación completa
def is_valid_move(T, C_i, c_actual, c_sig, pair, pendientes):
    # 1. adyacencia ortogonal
    if not is_adjacent(c_actual, c_sig):
        return False

    # 2. dentro del tablero
    if not inside_board(T, c_sig):
        return False

    # 3. celda vacía o destino
    if not cell_free_or_target(T, c_sig, pair):
        return False

    # 4. no repetir en el camino
    if not not_in_path(C_i, c_sig):
        return False

    # 5. no cruzar otros caminos
    if not not_other_pair_path(T, c_sig, pair):
        return False

    # 6. destino aún alcanzable
    if not reachable(T, c_sig, pair):
        return False

    return True

