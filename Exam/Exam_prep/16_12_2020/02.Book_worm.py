def is_valid(pos, size):
    return 0 <= pos[0] < size and 0 <= pos[1] < size


text = [x for x in input()]

n = int(input())

matrix = []
p_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == 'P':
            p_pos = [row, col]
    matrix.append(line)


m = int(input())

for _ in range(m):
    command = input()
    dir_changes = directions[command]
    new_pos = [p_pos[0] + dir_changes[0], p_pos[1] + dir_changes[1]]

    if is_valid(new_pos, n):
        matrix[p_pos[0]][p_pos[1]] = "-"
        if matrix[new_pos[0]][new_pos[1]] != "-":
            text.append(matrix[new_pos[0]][new_pos[1]])
        p_pos = new_pos
        matrix[p_pos[0]][p_pos[1]] = "P"

    else:
        if text:
            text.pop()

print("".join(text))
[print(''.join(el)) for el in matrix]

