from Tic_Tac_Toe.constants import position_mapper
from Tic_Tac_Toe.helper import get_row_col


def check_position_in_range(pos):
    if 1 <= pos <= 9:
        return True
    return False


def is_place_available(board, pos):
    row, col = get_row_col(pos)
    if not board[row][col] == " ":
        return False
    return True
