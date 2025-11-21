# path.py
# -----------------------------------------------------------------------
# Funciones auxiliares para manejar caminos C_i como listas (pilas) de celdas.

def start_path(pair):
    """
    Inicializa el camino C_i con el punto inicial de la pareja.
    """
    (_, start, _) = pair
    return [start]


def push_cell(C_i, cell):
    """
    Agrega una celda al final del camino C_i.
    """
    C_i.append(cell)


def pop_cell(C_i):
    """
    Elimina la última celda del camino C_i y la devuelve.
    """
    if not C_i:
        return None
    return C_i.pop()
