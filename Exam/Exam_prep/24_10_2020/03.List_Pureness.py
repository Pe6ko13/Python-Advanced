# from collections import deque
#
#
# def best_list_pureness(line, k):
#     def calc_pureness(line):
#         pureness = 0
#         for (index, value) in enumerate(line):
#             pureness += index * value
#         return pureness
#
#
#     line = deque(line)
#     k = min(k, len(line))
#     best_rotation = 0
#     best_pure = calc_pureness(line)
#     for rot in range(k + 1):
#         current_pureness = calc_pureness(line)
#         if best_pure < current_pureness:
#             best_rotation = rot
#             best_pure = current_pureness
#         line.rotate()
#
#
#     return f'Best pureness {best_pure} after {best_rotation} rotations'


from collections import deque

def best_list_pureness(numbers, k):
    data = {}
    numbers = deque(numbers)

    for rotation in range(k+1):
        if rotation == len(numbers):
            break
        result = sum([index*number for index, number in enumerate(numbers)])
        data.update({rotation: result})
        numbers.rotate()

    max_pureness = max(data.values())
    for key, val in data.items():
        if max_pureness == val:
            return f"Best pureness {val} after {key} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
