n = int(input())

matrix = []

matrix = [
    [int(x) for x in input().split(', ')]
    for _ in range(n)
]


a = [matrix[i][i] for i in range(n)]
b = [matrix[i][n -1 -i] for i in range(n)]

print(f"First diagonal: {', '.join([str(x) for x in a])}. Sum: {sum(a)}")
print(f"Second diagonal: {', '.join([str(x) for x in b])}. Sum: {sum(b)}")