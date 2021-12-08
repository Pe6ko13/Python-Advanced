def is_valid(pl_pos, range):
    return 0 <= pl_pos[0] < range and 0 <= pl_pos[1] < range


n = 5
field = []
t_count = 0
plane_pos = []
hit_targets = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for i in range(5):
    line = input().split()
    for j in range(5):
        if line[j] == 'A':
            plane_pos = [i, j]
        elif line[j] == 'x':
            t_count += 1
    field.append(line)

new_count = t_count

m = int(input())

for _ in range(m):
    command = input().split()
    direct = command[1]
    move = directions[direct]

    if command[0] == 'shoot':
        next_pos = [plane_pos[0] + move[0], plane_pos[1] + move[1]]
        while is_valid(next_pos, n):
            if field[next_pos[0]][next_pos[1]] == "x":
                field[next_pos[0]][next_pos[1]] = '.'
                hit_targets.append([next_pos[0], next_pos[1]])
                new_count -= 1
                if new_count == 0:
                    print(f"Training completed! All {t_count} targets hit.")
                break

            next_pos[0] += move[0]
            next_pos[1] += move[1]

    if command[0] == 'move':
        steps = int(command[2])
        new_dir = [move[0] * steps, move[1] * steps]
        new_pl_pos = [plane_pos[0] + new_dir[0], plane_pos[1] + new_dir[1]]

        if is_valid(new_pl_pos, n) and field[new_pl_pos[0]][new_pl_pos[1]] == '.':
            field[plane_pos[0]][plane_pos[1]] = "."
            field[new_pl_pos[0]][new_pl_pos[1]] = 'A'
            plane_pos = [new_pl_pos[0], new_pl_pos[1]]

if new_count != 0:
    print(f"Training not completed! {new_count} targets left.")

print('\n'.join([str(x) for x in hit_targets]))

[print(''.join(x)) for x in field]
