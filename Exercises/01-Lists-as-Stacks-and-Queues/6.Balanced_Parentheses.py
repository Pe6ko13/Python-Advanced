expression = input()
stack = []
balanced = True

for parentheses in expression:
    if parentheses in '[{(':
        stack.append(parentheses)
    elif parentheses in ']})':
        if len(stack) == 0:
            balanced = False
            break
        opening_parent = stack.pop()
        if f"{opening_parent}{parentheses}" not in ['[]', '{}', '()']:
            balanced = False
            break
if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')
