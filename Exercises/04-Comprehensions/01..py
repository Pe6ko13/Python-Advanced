n = int(input())

matrix = [[int(el) for el in input(). split(', ')] for _ in range(n)]
even_m = [[num for num in sublist if num % 2 == 0] for sublist in matrix]
# even_m = [num for sub in matrix for num in sub if num % 2 == 0]
print(even_m)


# matrix = [[int(el) for el in input(). split(', ') if int(el) % 2 == 0] for _ in range(n)]
# print(matrix)