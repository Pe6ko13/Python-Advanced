from Tic_Tac_Toe.logic import play


def print_board_positions():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def create_empty_board():
    return [[" ", " ", " "] for _ in range(3)]


def setup():
    player1 = input('Player 1 name: ')
    player2 = input('Player 2 name: ')
    player1_sign = input(f'{player1}, choose your sign (X or O): ').upper()
    while not player1_sign in ['X', 'O']:
        player1_sign = input(f'{player1}, choose your sign (X or O): ').upper()
    player2_sign = 'O' if player1_sign == 'X' else 'X'
    print(f"{player1} starts first")
    print_board_positions()
    board = create_empty_board()
    players = {player1: player1_sign, player2: player2_sign}
    turns_mapper = {0: player2, 1: player1}
    play(players, board, turns_mapper)


def start_game():
    setup()


if __name__ == '__main__':
    start_game()



