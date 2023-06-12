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
    for row in range(ROWS):
        print(" ")
        for col in range(COLS):
            print(board[row][col],end=' ')

create_board()
print_board()
