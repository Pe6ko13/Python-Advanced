from Tic_Tac_Toe.validator import check_position_in_range, is_place_available
from Tic_Tac_Toe.helper import get_row_col, print_current_board, is_winner, is_board_full


def play(players, board, turns):
    current_turn_count = 1
    while True:
        current_player = turns[current_turn_count % 2]
        # read position

        position = int(input(f"{current_player} choose a free position: "))
        # check if it is in ange:

        if check_position_in_range(position):
            # check is place available

            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player]
                print_current_board(board)

                # check if there is a winner

                if is_winner(board):
                    print(f'{current_player} win')
                    exit(0)
                if is_board_full(board):
                    print(f'GAME OVER! No Winner')
                    exit(0)
            else:
                print('Position is taken! Choose again')
                current_turn_count += 1

        current_turn_count += 1


