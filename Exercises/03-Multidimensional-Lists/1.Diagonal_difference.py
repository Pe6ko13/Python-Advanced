n = int(input())
sum_1= 0
sum_2 = 0
matrix = []
for i in range(n):
    matrix.append([int(el) for el in input().split()])
for i in range(n):
    sum_1 += matrix[i][i]
for j in range(n):
    sum_2 += matrix[len(matrix) - 1 - j][j]

difference = abs(sum_2 - sum_1)

print(difference)
