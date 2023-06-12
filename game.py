import sys
import random
import math

# 6 LINHAS
# 7 COLUNAS
# VALIDAR JOGADAS

ROWS = 6
COLS = 7
board = []

def create_board():
    for _ in range(ROWS):
        board.append([0]*COLS)

def print_board():
    for row in board:
        print(row)

create_board()
print_board()
