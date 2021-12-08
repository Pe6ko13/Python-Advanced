rows, cols = map(int, input().split())

matrix = []

for i in range(rows):
    matrix.append([el for el in input().split()])

command = input()

while not command == 'END':
    new_command = command.split()
    if new_command[0] == 'swap' and 0 < rows >= int(new_command[1]) and len(new_command) == 5:
        temp = matrix[int(new_command[1])][int(new_command[2])]
        matrix[int(new_command[1])][int(new_command[2])] = matrix[int(new_command[3])][int(new_command[4])]
        matrix[int(new_command[3])][int(new_command[4])] = temp
        for i in matrix:
            print(' '.join(i))
    else:
        print("Invalid input!")


    command = input()