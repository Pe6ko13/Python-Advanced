rows, cols = [int(el) for el in input().split()]

matrix = []
max_sum = 0
max_i = 0
max_j = 0

for rol in range(rows):
    matrix.append([int(el) for el in input().split()])

for start_row in range(rows - 2):
    for start_col in range(cols - 2):
        current_sum = 0
        for i in range(3):
            for j in range(3):
                current_sum += matrix[start_row + i][start_col + j]
        if max_sum < current_sum:
            max_sum = current_sum
            max_i = start_row
            max_j = start_col

print(f"Sum = {max_sum}")

for i in range(3):
    for j in range(3):
        print(matrix[max_i + i][max_j + j], end=' ')
    print()