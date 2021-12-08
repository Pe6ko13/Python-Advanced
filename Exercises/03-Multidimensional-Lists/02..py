# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in range(len(matrix)):
#     for j in range(len(matrix[row])):
#         print(matrix[row][j], end=" ")
#     print()

rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)

