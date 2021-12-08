from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottles = bottles.pop()

    current_cup -= current_bottles

    if current_cup <= 0:
        wasted_water += abs(current_cup)

    else:
        cups.appendleft(current_cup)

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in reversed(bottles)])}")

else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted_water}")



