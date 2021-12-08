board = []
kingpos = []
for row in range(8):
    line = [x for x in input().split()]
    for col in range(8):
        if line[col] == 'K':
            kingpos = [row, col]
    board.append(line)




matrix = []
for row in range(n):
    line = list(input())
    if 'P' in line:
        paris_pos = [row, line.index('P')]
    matrix.append(line)



for row in range(8):
    board.append([x for x in input().split()])
    if 'K' in board[row]:
        col = (board[row].index('K'))
        kingpos = [row, col]




board = [
    [2, 3, 4, 5],
    [3, 5, 7],
    [4, 6, 7, 8, 9]
]
for row in range(len(board)):
    for col in range(len(board[row])):
        print(board[row][col], end=' ')
    print()



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



def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False
