from collections import deque

kids = deque(input().split())
count = int(input())

while len(kids) > 1:
    kids.rotate(-count)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.pop()}")