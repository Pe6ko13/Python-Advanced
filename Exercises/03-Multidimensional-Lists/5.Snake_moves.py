# from collections import deque
#
# n, m = [int(n) for n in input().split(' ')]
#
# snake = deque(list(input()))
#
# for row in range(n):
#     s = ''
#     for col in range(m):
#         piece = snake.popleft()
#         s += piece
#         snake.append(piece)
#     if row % 2 == 0:
#         print(s)
#     else:
#        print(s[::-1])




def create_matrix(row, col):
    matrix = []
    for _ in range(row):
        matrix.append([])
        for _ in range(col):
            matrix[-1].append('')

    return matrix

n, m = input().split()
n, m = int(n), int(m)
text = input()

matrix = create_matrix(n, m)

col = 0
text_index = 0
  
for row in range(n):

    if row % 2 == 0:
        dir = 1
    else:
        dir = -1
    while 0 <= col < m:
        matrix[row][col] = text[text_index]
        if text_index + 1 == len(text):
            text_index = -1
        text_index += 1
        col += dir
    col -= dir
for i in range(len(matrix)):
    print(''.join(matrix[i]))
