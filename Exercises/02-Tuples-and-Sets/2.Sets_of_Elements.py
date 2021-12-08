n, m = input().split()
n, m = int(n), int(m)

set_a, set_b = set(), set()

for _ in range(n):
    set_a.add(input())

for _ in range(m):
    set_b.add(input())

print('\n'.join(set_a.intersection(set_b)))


