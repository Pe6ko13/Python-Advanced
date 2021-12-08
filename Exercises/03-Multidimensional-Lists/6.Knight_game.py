def read_board():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return matrix


def knights_attacking_each_other(matrix):
    knight_positions = find_all_knights(matrix)

    for row, col in knight_positions:
        positions_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]

        for position in positions_to_check:
            pos_row, pos_col = position
            if not (0 <= pos_row <= len(matrix) - 1):
                continue
            if not (0 <= pos_col <= len(matrix) - 1):
                continue
            if matrix[pos_row][pos_col] == 'K':
                return True

    return False


def find_all_knights(matrix):
    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'K':
                positions.append((i, j))

    return positions


def calculate_aggression(matrix, knight_positions):
    aggression_scores = {}
    for row, col in knight_positions:
        positions_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]

        attacked_count = 0
        for attacked_row, attacked_col in positions_to_check:
            if not 0 <= attacked_row <= len(matrix) - 1:
                continue
            if not 0 <= attacked_col <= len(matrix) - 1:
                continue
            if matrix[attacked_row][attacked_col] == 'K':

                attacked_count += 1
        aggression_scores[(row, col)] = attacked_count

    return aggression_scores


def find_max_aggression(aggression_scores):
    max_so_far = None
    max_pos = None
    for pos, aggression in aggression_scores.items():
        if max_so_far is None or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos

    return max_pos


def main():
    matrix = read_board()
    deleted_count = 0
    while knights_attacking_each_other(matrix) is True:
        knight_positions = find_all_knights(matrix)
        aggression_scores = calculate_aggression(matrix, knight_positions)

        row, col = find_max_aggression(aggression_scores)

        matrix[row][col] = '0'
        deleted_count += 1
    print(deleted_count)


main()
