numbers = [[int(x) for x in number.split()] for number in input().split('|')]
numbers.reverse()

# for seq in numbers:
#     for number in seq:
#         pass

numbers = [number for seq in numbers for number in seq]

print(' '.join([str(x) for x in numbers]))
