# def read_board():
#     board = []
#     for row in range(8):
#         line = [x for x in input().split()]
#         board.append(line)
#     return board
#
#
# def find_king_pos(board):
#     for row in range(8):
#         for col in range(8):
#             if board[row][col] == 'K':
#                 return row, col
#
#
# # def get_capturing_queens(board, king):
# #     rows_count = len(board)
# #     cols_count = len(board[0])
# #     (king_row, king_col) = king
# #     queen = []
# # # right:
# #     for col in range(king_col + 1, cols_count):
# #         if board[king_row][col] == 'Q':
# #             queen.append((king_row, col))
# #             break
# # # left:
# #     for col in range(king_col - 1, -1, -1):
# #         if board[king_row][col] == 'Q':
# #             queen.append((king_row, col))
# #             break
#
# def in_range(value, max_value):
#     return 0 <= value < max_value
#
#
# def search_with_deltas(board, king, deltas):
#     rows_count = len(board)
#     cols_count = len(board[0])
#     (king_row, king_col) = king
#     (delta_row, delta_col) = deltas
#
#     while in_range(king_row, rows_count) and in_range(king_col, cols_count):
#         if board[king_row][king_col] == 'Q':
#             return [king_row, king_col]
#
#         king_row += delta_row
#         king_col += delta_col
#
#
# def get_capturing_queens(board, king):
#     deltas = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
#     queen = [search_with_deltas(board, king, delta) for delta in deltas]
#     return [q for q in queen if q]
#
#
# def print_result(queen):
#     if queen:
#         for q in queen:
#             print(q)
#     else:
#         print('The king is safe!')
#
#
# board = read_board()
# king = find_king_pos(board)
# queens = get_capturing_queens(board, king)
#
# print_result(queens)


def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


matrix = []
n = 8

for _ in range(n):
    matrix.append(input().split())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1)
}

queens = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "Q":
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                while is_in_range(next_row, next_col, n):
                    if matrix[next_row][next_col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        queens.append([row, col])
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if queens:
    [print(pos) for pos in queens]
else:
    print("The king is safe!")