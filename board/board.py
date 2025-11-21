# board.py
# -----------------------------------------------------------------------
# Funciones auxiliares para manipular la matriz del tablero T[N][M].

def get_dimensions(T):
    """
    Devuelve las dimensiones del tablero T.
    """
    return len(T), len(T[0])


def is_inside(T, x, y):
    """
    Verifica si la posición (x, y) está dentro del tablero.
    """
    N, M = get_dimensions(T)
    return 0 <= x < N and 0 <= y < M


def is_empty(T, x, y):
    """
    Devuelve True si la celda T[x][y] está vacía.
    """
    return T[x][y] == "."


def get_cell(T, x, y):
    """
    Retorna el contenido de la celda T[x][y].
    """
    return T[x][y]


def set_cell(T, x, y, symbol):
    """
    Escribe el símbolo 'symbol' en la celda T[x][y].
    """
    T[x][y] = symbol


def clear_cell(T, x, y):
    """
    Restaura la celda T[x][y] a su estado vacío.
    """
    T[x][y] = "."


def get_neighbors(x, y):
    """
    Devuelve las cuatro celdas ortogonales vecinas a (x, y).
    """
    return [
        (x + 1, y),   # abajo
        (x - 1, y),   # arriba
        (x, y + 1),   # derecha
        (x, y - 1)    # izquierda
    ]


def print_board(T):
    """
    Imprime el tablero en forma legible. Útil para depuración.
    """
    for fila in T:
        print(" ".join(fila))
