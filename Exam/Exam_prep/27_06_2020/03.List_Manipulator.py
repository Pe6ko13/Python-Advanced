# from collections import deque
#
#
# def list_manipulator(list_obj, operator, position, *args):
#     new_list = deque(list_obj)
#
#     if operator == 'add':
#         assert len(args) > 0
#         if position == 'beginning':
#             new_list = deque(args) + new_list
#         elif position == 'end':
#             new_list += deque(args)
#     elif operator == 'remove':
#         assert 0 <= len(args) <= 1
#         n = args[0] if len(args) == 1 else 1
#         fn = new_list.popleft if position == 'beginning' else new_list.pop
#         for _ in range(n):
#             fn()
#
#     return list(new_list)


from collections import deque


def list_manipulator(numbers, command, position, *args):
    numbers = deque(numbers)

    if command == 'add':
        if position == 'beginning':
            for elements in reversed(args):
                numbers.appendleft(elements)
        elif position == 'end':
            for elements in args:
                numbers.append(elements)

    elif command == 'remove':
        if position == 'beginning':
            if args:
                for i in range(*args):
                    numbers.popleft()
            else:
                numbers.popleft()

        elif position == 'end':
            if args:
                for j in range(*args):
                    numbers.pop()
            else:
                numbers.pop()

    return list(numbers)






print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))


