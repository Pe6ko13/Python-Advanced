num = int(input())
stack = []

for index in range(num):
    command = input().split()
    if command[0] == '1':
        stack.append(command[1])

    if command[0] == '2':
        if len(stack) >0:

            stack.pop()

    if command[0] == '3':
        if len(stack) > 0:
            print(max(stack))
    if command[0] == '4':
        if len(stack) > 0:

            print(min(stack))

reversed_numbers = []

for i in range(len(stack)):
    reversed_numbers.append(stack.pop())
print(', '.join(reversed_numbers))
