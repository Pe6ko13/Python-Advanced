rows, columns = [int(el) for el in input().split(", ")]

matrix = []
result = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])   #/   current_row_el = []
    #                                                             for el in input().split(', '):
    #                                                                 current_row_el.append(int(el))
    #                                                             matrix.append(current_row_el)

    result += sum(matrix[row])                                #/  for row in range(rows):
#                                                                     for col in range(columns):
 #                                                                        result += matrix[row][col]
print(result)
print(matrix)
