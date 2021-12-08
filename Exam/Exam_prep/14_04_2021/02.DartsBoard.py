import math

def in_range(row, col):
    if row in range(7) and col in range(7):
        return True
    return False


def is_number(el):
    try:
        return int(el)
    except Exception:
        return False


N = 7

player1, player2 = input().split(', ')
points = {player1: 501, player2: 501}

turns_count = 1
player_turn = {0: player2, 1: player1}

matrix = []

for _ in range(N):
    matrix.append(input().split())

while True:
    row, col = [int(el) for el in input()[1:-1].split(', ')]
    if in_range(row, col):
        number = is_number(matrix[row][col])
        if number:
            points[player_turn[turns_count % 2]] -= number

        current_points = sum([
            int(matrix[0][col]),
            int(matrix[-1][col]),
            int(matrix[row][0]),
            int(matrix[row][-1])
        ])

        if matrix[row][col] == 'D':
            points[player_turn[turns_count % 2]] -= current_points*2

        if matrix[row][col] == 'T':
            points[player_turn[turns_count % 2]] -= current_points*3

        if matrix[row][col] == 'B':
            print(f"{player_turn[turns_count%2]} won the game with {math.ceil(turns_count/2)} throws!")
            exit(0)

        if points[player1] <= 0 or points[player2] <= 0:
            break

    turns_count += 1

print(f"{player_turn[turns_count % 2]} won the game with {math.ceil(turns_count / 2)} throws!")


