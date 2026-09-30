import numpy as np

FILAS = 6
COLUMNAS = 7
VACIO = 0
JUGADOR = 1
AGENTE = 2

def crear_tablero():
    return np.zeros((FILAS, COLUMNAS), dtype=int)

def es_columna_valida(tablero, col):
    return tablero[FILAS - 1][col] == 0

def obtener_siguiente_fila_libre(tablero, col):
    for f in range(FILAS):
        if tablero[f][col] == 0:
            return f

def soltar_ficha(tablero, fila, col, ficha):
    tablero[fila][col] = ficha

def obtener_columnas_validas(tablero):
    return [c for c in range(COLUMNAS) if es_columna_valida(tablero, c)]

def verificar_victoria(tablero, ficha):
    # Horizontales
    for c in range(COLUMNAS - 3):
        for f in range(FILAS):
            if tablero[f][c] == ficha and tablero[f][c+1] == ficha and tablero[f][c+2] == ficha and tablero[f][c+3] == ficha:
                return True
    # Verticales
    for c in range(COLUMNAS):
        for f in range(FILAS - 3):
            if tablero[f][c] == ficha and tablero[f+1][c] == ficha and tablero[f+2][c] == ficha and tablero[f+3][c] == ficha:
                return True
    # Diagonales (+)
    for c in range(COLUMNAS - 3):
        for f in range(FILAS - 3):
            if tablero[f][c] == ficha and tablero[f+1][c+1] == ficha and tablero[f+2][c+2] == ficha and tablero[f+3][c+3] == ficha:
                return True
    # Diagonales (-)
    for c in range(3, COLUMNAS):
        for f in range(FILAS - 3):
            if tablero[f][c] == ficha and tablero[f+1][c-1] == ficha and tablero[f+2][c-2] == ficha and tablero[f+3][c-3] == ficha:
                return True
    return False

def es_nodo_terminal(tablero):
    return verificar_victoria(tablero, JUGADOR) or verificar_victoria(tablero, AGENTE) or len(obtener_columnas_validas(tablero)) == 0