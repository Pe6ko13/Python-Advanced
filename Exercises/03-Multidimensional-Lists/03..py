rows = cols = int(input())

matrix =[]
result = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split()])
    result += matrix[row][row]
    

# for row in range(rows):
#     for col in range(cols):
#         if row == col:
#            result += matrix[row][col]

print(result)