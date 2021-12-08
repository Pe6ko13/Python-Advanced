# def get_magic_triangle(n):
#     triangle = []
#
#     for i in range(n):
#         triangle.append([0] * (i + 1))
#
#     triangle[0][0] = 1
#
#     for row_idx, row in enumerate(triangle):
#         for col_idx, col in enumerate(row):
#             left = right = 0
#             if (row_idx, col_idx) == (0, 0):
#                 continue
#
#             if (0 <= row_idx < n) and (0 <= col_idx - 1 < len(triangle[row_idx - 1])):
#                 left = triangle[row_idx - 1][col_idx - 1]
#             if (0 <= row_idx < n) and (0 <= col_idx < len(triangle[row_idx - 1])):
#                 right = triangle[row_idx - 1][col_idx]
#
#             triangle[row_idx][col_idx] = left + right
#
#     return triangle


# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for row in range(2, n):
#         new_row = []
#         for col in range(0, row + 1):
#             if col - 1 < 0:
#                 new_row.append(1)
#             elif col >= len(triangle[row - 1]):
#                 new_row.append(1)
#             else:
#                 upper_left = triangle[row - 1][col - 1]
#                 upper_right = triangle[row - 1][col]
#                 new_value = upper_right + upper_left
#                 new_row.append(new_value)
#         triangle.append(new_row)
#
#     return triangle


def get_magic_triangle(n):
    triangle = [[1] * row for row in range(1, n + 1)]
    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    return triangle


triangle = get_magic_triangle(5)
print(triangle)


