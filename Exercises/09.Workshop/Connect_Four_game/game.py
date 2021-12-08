from Connect_Four_game.helper import find_empty_space, is_stalemate, has_player_won
from pprint import pprint

number_rows = 6
number_cols = 7


def main():
    board = [[0] * number_cols for _ in range(number_rows)]
    # board = read_board()
    player1, player2 = 1, 2

    while True:
        try:
            col = int(input())
        except ValueError:
            continue

        col -= 1

        if not 0 <= col < number_cols:
            continue

        row = find_empty_space(board, col)
        if row == -1:
            continue

        board[row][col] = player1
        if is_stalemate(board):
            print("GAME OVER")
            print("STALEMATE")
            break

        if has_player_won(board, (row, col)):
            print((f'Player {player1} won!'))
            break

        pprint(board)
        player1, player2 = player2, player1


def read_board(rows):
    board = []
    for row in rows:
        row = [int(x) for x in row.split()]
        board.append(row)
    return board


if __name__ == '__main__':
    main()