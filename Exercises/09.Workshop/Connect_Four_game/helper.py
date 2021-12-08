DOWN = RIGHT = 1
LEFT = UP = -1
STAY = 0
number_rows = 6
number_cols = 7

def find_empty_space(board, column):
    for row in range(0, number_rows):
        if board[row][column] != 0:
            return row - 1
    return number_rows - 1


def is_stalemate(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True


def get_position_in_direction(board, start_position, direct):
    start_row, start_col = start_position
    move_by_row, move_by_col = direct

    positions = []

    current_row, current_col = start_row, start_col
    for _ in range(3):
        current_row += move_by_row
        current_col += move_by_col

        if not 0 <= current_row < len(board):
            return positions
        if not 0 <= current_col < len(board[current_row]):
            return positions

        positions.append(board[current_row][current_col])

    return positions


# def player_won(board, last_position):
#
#     directions = [
#         (STAY, RIGHT),
#         (DOWN, RIGHT),
#         (DOWN, STAY),
#         (DOWN, LEFT),
#         (STAY, LEFT),
#         (UP, LEFT),
#         (UP, RIGHT),
#     ]
#     last_row, last_col = last_position
#
#     for direct in directions:
#         positions = get_position_in_direction(board, last_position, direct)
#         if len(positions) == 4 and all([pos == board[last_row][last_col] for pos in positions]):
#             return True
#     return False


def has_four_consecutive(target_line, target):
    count = 0
    for el in target_line:
        if el == target:
            count += 1
        else:
            count = 0

        if count == 4:
            return True
    return False


def has_player_won(board, last_position):

        LEFT_HOR = (STAY, LEFT)
        RIGHT_HOR = (STAY, RIGHT)
        UP_VER = (UP, STAY)
        DOWN_VER = (DOWN, STAY)
        UP_RIGHT_DIA = (UP, RIGHT)
        DOWN_RIGHT_DIA = (DOWN, RIGHT)
        DOWN_LEFT_DIA = (DOWN, LEFT)
        UP_LEFT_DIA = (UP, LEFT)

        directions = [
            (LEFT_HOR, RIGHT_HOR),
            (UP_VER, DOWN_VER),
            (DOWN_LEFT_DIA, UP_RIGHT_DIA),
            (UP_LEFT_DIA, DOWN_RIGHT_DIA),
        ]
        start_row, start_col = last_position
        for backward_direction, forward_direction in directions:
            backward_position = get_position_in_direction(board, last_position, backward_direction)
            forward_position = get_position_in_direction(board, last_position, forward_direction)

            target_line = list(reversed(backward_position)) + [board[start_row][start_col]] + forward_position

            if has_four_consecutive(target_line, target=board[start_row][start_col]):
                return True
        return False

