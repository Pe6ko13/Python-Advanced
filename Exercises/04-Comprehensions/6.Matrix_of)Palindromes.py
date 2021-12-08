n, m = [int(x) for x in input().split()]

matrix = []
base = ord('a')
for row in range(n):
    matrix.append([])
    for col in range(m):
        first_letter = chr(row + base)
        middle_letter = chr(row + col + base)
        matrix[-1].append(f'{first_letter}{middle_letter}{first_letter}')
print('\n'.join(' '.join([str(x) for x in row]) for row in matrix))

