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
vazio = '⚪'
simbolo_j1= '🟡'
simbolo_j2= '🔴'

def create_board():
    for _ in range(ROWS):
        board.append([vazio] * COLS)

def print_board():
    for row in range(ROWS-1, -1, -1):
        print(" ")
        for col in range(COLS):
            print(board[row][col],end=' ')

def add_token(board, col, token):
    if board[ROWS -1][col] == vazio:
        for row in range(ROWS):
            if(board[row][col] == vazio):
                if(token == "J1"):
                    board[row][col] = (simbolo_j1)
                elif(token == "J2"):
                    board[row][col] = (simbolo_j2)
                break

def check_win(board, simbolo):
    # CHECK HORIZONTAL WIN
    for col in range(COLS -3):
        for row in range(ROWS):
            if board[row][col] == simbolo and board[row][col+1] == simbolo and board[row][col+2] == simbolo and board[row][col+3] == simbolo:
                return True
    #  CHECK VERTICAL WIN       
    for col in range(COLS):
        for row in range(ROWS-3):
            if board[row][col] == simbolo and board[row+1][col] == simbolo and board[row+2][col] == simbolo and board[row+3][col] == simbolo:
                return True
            
    # CHECK DIAGONAL DOWN
    for col in range(COLS):
        for row in range(3, ROWS):
            if board[row][col] == simbolo and board[row-1][col+1] == simbolo and board[row-2][col+2] == simbolo and board[row-3][col+3] == simbolo:
                return True
    
    # CHECK DIAGONAL UP
    for col in range(COLS):
            for row in range(ROWS - 3):
                if board[row][col] == simbolo and board[row+1][col+1] == simbolo and board[row+2][col+2] == simbolo and board[row+3][col+3] == simbolo:
                    return True
create_board()
print_board()

while winner == False:
    if turn % 2 == 0:
        print('\nVez do jogador 1')
        J1 = int(input('\nSelecione uma coluna (0-6): '))
        turn += 1
        add_token(board, J1, 'J1')
        if check_win(board, simbolo_j1):
            print('Jogador 1 venceu!')
            winner = True
        print_board()
    else:
        print('\nVez do jogador 2')
        J2 = int(input('\nSelecione uma coluna (0-6): '))
        turn +=1
        add_token(board, J2, 'J2')
        if check_win(board, simbolo_j2):
            print('Jogador 2 venceu!')
            winner = True
        print_board()
