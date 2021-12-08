01.

text = list(input())
result = []
while len(text) > 0:
    result.append(text.pop())

print(''.join(result))


02.

text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))


