board = int(input())
mines_number = int(input())

minefield = [([0] * board) for i in range(board)]

neighbour_cells = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
]


def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def get_num(r, c, field):
    mines = 0
    for row, col in neighbour_cells:
        if is_in_range(row + r, col + c, board):
            if field[row + r][col + c] == '*':
                mines += 1
    return mines


def fill_board(mine_field):
    for row in range(len(mine_field)):
        for col in range(len(mine_field)):
            if not mine_field[row][col] == '*':
                mine_field[row][col] = get_num(row, col, mine_field)


for _ in range(mines_number):
    r, c = eval(input())
    minefield[r][c] = '*'
    fill_board(minefield)



for i in minefield:
    print(' '.join([str(x) for x in i]))
