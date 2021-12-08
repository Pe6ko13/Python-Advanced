from math_operation.contents import operation_mapper

num1, operator, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

print(operation_mapper[operator](num1, num2))

