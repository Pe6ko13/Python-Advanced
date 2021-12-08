rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

max_sum = 0
position = None

for row in range(rows - 1, 0, -1):
    current_sum = 0
    for col in range(cols - 1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row-1][col - 1]
    if current_sum >= max_sum:
        max_sum = current_sum
        position = (row, col)

row, col = position
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 1], matrix[row][col])
print(max_sum)


2.
def read_matrix():
    rows, cols = map(int, input().split(', '))
    matrix = []
    for row in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def get_sum_submatrix(matrix, row, col, size):
    the_sum = 0
    for r in range(row, row + size):
        for c in range(col, col + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix_sum(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_submatrix(matrix, 0, 0, submatrix_size)

    for row in range(len(matrix) - submatrix_size + 1):
        for col in range(len(matrix[row]) - submatrix_size + 1):
            current_sum = get_sum_submatrix(matrix, row, col, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row
                best_column_index = col
    return  (best_row_index, best_column_index)

def print_result(coordinates, size):
    row, col = coordinates
    for r in range(row, row + size):
        ro = []
        for c in range(col, col + size):
            ro.append(matrix[r][c])
        print(' '.join(str(x) for x in ro))
    print(get_best_submatrix_sum(matrix, row, col, size))


submatrix_size = 2

matrix = read_matrix()
coordinates = get_best_submatrix_sum(matrix, submatrix_size)
print_result(coordinates, submatrix_size)
