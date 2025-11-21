# pretty_print.py
# -----------------------------------------------------------------------
# Utilidades para mostrar el tablero y estructuras de forma legible.

def print_board_with_indices(T):
    """
    Imprime el tablero T mostrando índices de filas y columnas,
    útil para depuración y para entender las coordenadas (x, y).
    """
    if not T:
        print("(tablero vacío)")
        return

    N = len(T)
    M = len(T[0])

    # Encabezado de columnas
    header = "    " + " ".join(f"{j:2d}" for j in range(M))
    print(header)
    print("   " + "-" * (3 * M))

    # Filas con índice
    for i, fila in enumerate(T):
        fila_str = " ".join(f"{c:2s}" for c in fila)
        print(f"{i:2d}| {fila_str}")


def print_pairs(P):
    """
    Imprime la lista de parejas P de forma legible.
    """
    if not P:
        print("No hay parejas detectadas.")
        return

    print("Parejas detectadas:")
    for p in P:
        (symbol, (x1, y1), (x2, y2)) = p
        print(f"  símbolo '{symbol}': ({x1},{y1}) -> ({x2},{y2})")
