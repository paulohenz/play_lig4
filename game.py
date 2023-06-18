import sys
import random
import math
import pygame

# 6 LINHAS
# 7 COLUNAS
# VALIDAR JOGADAS

ROWS = 6
COLS = 7
board = []
winner = False
turn = 0
empty_token = "⚪"
J1_token = "🟡"
J2_token = "🔴"


def create_board():
    for _ in range(ROWS):
        board.append([empty_token] * COLS)


def print_board():
    for row in range(ROWS - 1, -1, -1):
        print(" ")
        for col in range(COLS):
            print(board[row][col], end=" ")


def add_token(board, col, token):
    if board[ROWS - 1][col] == empty_token:
        for row in range(ROWS):
            if board[row][col] == empty_token:
                if token == "J1":
                    board[row][col] = J1_token
                elif token == "J2" or token == "Computador":
                    if jogadores == 1:
                        token == "J2"
                        board[row][col] = J2_token
                    else:
                        jogadores == 2
                        token == "Computador"
                        board[row][col] = J2_token
                break


def check_win(board, token):
    # CHECK HORIZONTAL WIN
    for col in range(COLS - 3):
        for row in range(ROWS):
            if (
                board[row][col] == token
                and board[row][col + 1] == token
                and board[row][col + 2] == token
                and board[row][col + 3] == token
            ):
                return True
    #  CHECK VERTICAL WIN
    for col in range(COLS):
        for row in range(ROWS - 3):
            if (
                board[row][col] == token
                and board[row + 1][col] == token
                and board[row + 2][col] == token
                and board[row + 3][col] == token
            ):
                return True

    # CHECK DIAGONAL DOWN
    for col in range(COLS - 3):
        for row in range(3, ROWS):
            if (
                board[row][col] == token
                and board[row - 1][col + 1] == token
                and board[row - 2][col + 2] == token
                and board[row - 3][col + 3] == token
            ):
                return True

    # CHECK DIAGONAL UP
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if (
                board[row][col] == token
                and board[row + 1][col + 1] == token
                and board[row + 2][col + 2] == token
                and board[row + 3][col + 3] == token
            ):
                return True

while True:
    jogadores = int(input("Escolha uma opção: [1 - Humano/Humano 2 - Humano/Computador] "))
    if jogadores == 1 or jogadores == 2:
        break
    else:
        print("Opção Inválida! Escolha 1 ou 2 ")


create_board()
print_board()



while winner == False:
    if turn % 2 == 0:
        print("\nVez do jogador 1")
        while True:
            J1 = int(input("\nSelecione uma coluna (0-6): "))
            if J1 == 0 or J1 == 1 or J1 == 2 or J1 == 3 or J1 == 4 or J1 == 5 or J1 == 6:
                break
            else:
                print("Opção Inválida! Escolha um número de 0 a 6")
        turn += 1
        add_token(board, J1, "J1")
        if check_win(board, J1_token):
            print("Jogador 1 venceu!")
            winner = True
        print_board()
    else:
        if jogadores == 1:
            print("\nVez do jogador 2")
            while True:
                J2 = int(input("\nSelecione uma coluna (0-6): "))
                if J2 == 0 or J2 == 1 or J2 == 2 or J2 == 3 or J2 == 4 or J2 == 5 or J2 == 6:
                    break
                else:
                    print("Opção Inválida! Escolha um número de 0 a 6")
            turn += 1
            add_token(board, J2, "J2")
        elif jogadores == 2:
            print("\nVez do Computador")
            J2 = random.randint(0,6)
            print(f"\nO Computador selecionou a coluna {J2}")
            turn += 1
            add_token(board, J2, "J2")
        if check_win(board, J2_token):
            if jogadores == 1:
                print("Jogador 2 venceu!")
                winner = True
            elif jogadores == 2:
                print("Computador Venceu!")
                winner = True
        print_board()
