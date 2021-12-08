rows, cols = map(int, input().split())

matrix = []
count = 0

for row in range(rows):
    matrix.append(input().split())

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            count += 1
print(count)