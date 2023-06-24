import random

ROWS = 6
COLS = 7
board = []
winner = False
turn = 0
empty_token = "⚪"
J1_token = "🟡"
J2_token = "🔴"
PC_token = "🟢"


def create_board():
    for _ in range(ROWS):
        board.append([empty_token] * COLS)


def print_board():
    for row in range(ROWS - 1, -1, -1):
        print(" ")
        for col in range(COLS):
            print(board[row][col], end=" ")
    print("\n")
    print("\n=============================")

def add_token(board, col, token):
    if board[ROWS - 1][col] == empty_token:
        for row in range(ROWS):
            if board[row][col] == empty_token:
                if token == "J1":
                    board[row][col] = J1_token
                elif token == "J2":
                    board[row][col] = J2_token
                else:
                    board[row][col] = PC_token
                break
        return True
    else:
        return False

def check_draw():
    is_empty = False
    for col in range(COLS):
        if not is_empty:
            if board[ROWS - 1][col] == empty_token:
                is_empty = True
            else:
                is_empty = False
    if not is_empty:
        return True


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

def play_turn(player):
    print(f"\nVez do {player}")
    while True:
        if player == 'PC':
            selected_col = random.randint(0,6)
        else:
            selected_col = int(input("\nSelecione uma coluna (0-6): "))
        if selected_col >= 0 and selected_col < COLS:
            if add_token(board, selected_col, player):
                break
            else:
                print("Coluna cheia! Jogue novamente.")
        else:
            print("Opção inválida! Escolha um número de 0 a 6")

while True:
    players = int(input("Digite 1 para jogar contra o PC e 2 para jogar contra outro jogador: "))
    if players == 1 or players == 2:
        break
    else:
        print("Opção Inválida! Escolha 1 ou 2 ")


create_board()
print_board()

while winner == False:
    if turn % 2 == 0:
        play_turn("J1")
        turn += 1
        if check_win(board, J1_token):
            print("Jogador 1 venceu!")
            winner = True
        if check_draw():
            print('O jogo empatou!')
            break
        print_board()
    else:
        if players == 2:
            play_turn("J2")
            turn += 1
            if check_win(board, J2_token):
                print("Jogador 2 venceu!")
                winner = True
            if check_draw():
                print('O jogo empatou!')
                break
            print_board()
        elif players == 1:
            play_turn("PC")
            turn += 1
            if check_win(board, PC_token):
                print("Computador venceu!")
                winner = True
            if check_draw():
                print('O jogo empatou!')
                break
            print_board()

