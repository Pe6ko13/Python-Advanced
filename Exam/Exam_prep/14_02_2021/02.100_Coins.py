def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


n = int(input())

matrix = []
player_pos = []
coins = 0
steps = []

for row in range(n):
    line = input().split()
    if 'P' in line:
        player_pos = [row, line.index('P')]
    matrix.append(line)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

while True:
    command = input()
    if command in directions:
        next_row, next_col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]

        if is_in_range(next_row, next_col, n) and not matrix[next_row][next_col] == 'X':
            coins += int(matrix[next_row][next_col])
            steps.append([next_row, next_col])
        else:
            coins //= 2
            print(f"Game over! You've collected {coins} coins.")
            break

        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break

        player_pos = [next_row, next_col]

print('Your path:')
[print(x) for x in steps]