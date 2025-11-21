# conver.py 
# -------------------------------------------------------
# Este módulo se encarga de leer y convertir los archivos de entrada del 
# problema Numberlink al formato interno usado por el programa.

def load_board(file_path):
    tablero = []

    with open(file_path, "r") as file:
        # Leer dimensiones
        header = file.readline().strip().split()
        if len(header) != 2:
            raise ValueError("La primera línea debe contener N y M.")
        N = int(header[0])
        M = int(header[1])
        # Leer exactamente N filas
        for i in range(N):
            linea = file.readline()
            # Asegurar longitud mínima
            if linea is None:
                raise ValueError("Archivo incompleto: faltan filas del tablero.")
            # Conservar los espacios en blanco
            linea = linea.rstrip("\n")  
            # Si la línea es más corta, completar con espacios
            if len(linea) < M:
                linea = linea + " " * (M - len(linea))
            # Si es más larga, recortar
            if len(linea) > M:
                linea = linea[:M]
            # Convertir cada carácter a una celda
            fila = []
            for c in linea:
                if c == " ":
                    fila.append(".")   # convertir espacio en celda vacía
                else:
                    fila.append(c)
            tablero.append(fila)
    return tablero


def print_board(T):
    for fila in T:
        print(" ".join(fila))
