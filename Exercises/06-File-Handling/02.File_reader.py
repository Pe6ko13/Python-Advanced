file = open("numbers.txt")
result = 0

for line in file:
    result += int(line)
file.close()
print(result)


# 2

print(sum([int(line) for line in open('numbers.txt')]))



# 3

with open('numbers.txt') as file:
    result = 0
    for line in file:
        result += int(line)
    print(result)