# main.py
# -----------------------------------------------------------------------
# Archivo principal para cargar, mostrar y resolver un tablero de Numberlink.

import sys
from board import load_board
from model import extract_pairs
from solver import solve_board
from utils import print_board_with_indices, print_pairs

if __name__ == "__main__":

    # Leer el argumento de la línea de comandos
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <ruta_del_archivo_de_entrada>")
        print("Ejemplo:")
        print("   python3 main.py inputs/numberlink_00-2.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    # Cargar tablero
    try:
        T = load_board(file_path)
    except Exception as e:
        print(f"Error al cargar el tablero: {e}")
        sys.exit(1)

    # Detectar parejas
    P = extract_pairs(T)

    print("TABLERO INICIAL:")
    print_board_with_indices(T)
    print("\nPAREJAS DETECTADAS:")
    print_pairs(P)

    print("\nResolviendo...\n")

    # Intentar resolver el tablero
    solved = solve_board(T, P)

    if solved:
        print("¡SOLUCIÓN ENCONTRADA!\n")
        print_board_with_indices(T)
    else:
        print("NO SE ENCONTRÓ SOLUCIÓN :(")
