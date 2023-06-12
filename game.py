import sys
import random
import math

# 6 LINHAS
# 7 COLUNAS
# VALIDAR JOGADAS

ROWS = 6
COLS = 7
board = []
winner = False
turn = 0


def create_board():
    for _ in range(ROWS):
        board.append(['⚪'] * COLS)

def print_board():
    for row in range(ROWS-1, -1, -1):
        print(" ")
        for col in range(COLS):
            print(board[row][col],end=' ')

def add_token(board, col, token):
    if board[ROWS -1][col] == '⚪':
        pass
create_board()
print_board()

while winner == False:
    if turn % 2 == 0:
        print('\nVez do jogador 1')
        J1 = int(input('\nSelecione uma coluna (0-6): '))
        turn += 1
        add_token(board, J1, 'J1')
        print_board()
    else:
        print('\nVez do jogador 2')
        J2 = int(input('\nSelecione uma coluna (0-6): '))
        turn +=1
        print_board()
