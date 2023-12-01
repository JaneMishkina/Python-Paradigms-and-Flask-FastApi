"""Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера."""

def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
            return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0
    draw_board(board)

    for _ in range(9):
        row, col = map(int, input(f"Игрок {players[player_index]}, введите строку и колонку (нумерация с 1): ").split())
        row -= 1
        col -= 1
        if board[row][col] == " ":
            board[row][col] = players[player_index]
            draw_board(board)
        if check_winner(board, players[player_index]):
            print(f"Игрок {players[player_index]} победил!")
            return
        player_index = (player_index + 1) % 2

    draw_board(board)
    print("Игра окончена. Ничья!")

if __name__ == "__main__":
    main()
