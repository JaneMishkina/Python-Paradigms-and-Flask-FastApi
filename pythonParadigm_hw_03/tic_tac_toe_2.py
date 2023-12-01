"""Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера."""


# добавлена проверка, чтобы не занимали заполненную клетку

def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i * 3 + j], "|", end=" ")
        print("\n-------------")


def check_win(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return True
    return False


def tic_tac_toe():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = 0
    turns = 0

    while turns < 9:
        display_board(board)
        print("Ход игрока", players[current_player])
        move = int(input("Выберите номер клетки для хода (от 1 до 9): ")) - 1

        if move < 0 or move >= 9 or board[move] != " ":
            print("Некорректный ход. Попробуйте снова.")
            continue

        board[move] = players[current_player]
        turns += 1

        if check_win(board):
            display_board(board)
            print("Игрок", players[current_player], "победил!")
            return

        current_player = (current_player + 1) % 2

    display_board(board)
    print("Ничья!")


tic_tac_toe()
