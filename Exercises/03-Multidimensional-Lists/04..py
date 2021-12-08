n = int(input())

matrix = []
position = None

for row in range(n):
    matrix.append(list(input()))

symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

# print(position if position else f"{symbol} does not occur in the matrix")
if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")