from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())
matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)
        continue

    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0:
        if males:
            females.appendleft(female)
            males.pop()
            continue

    elif female % 25 == 0:
        if females:
            males.append(male)
            females.popleft()
            continue

    if female == male:
        matches += 1

    else:
        males.append(male - 2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(c) for c in reversed(males))}")
else:
    print("Males left: none")
# print(f"Males left: {'none' if not males else ', '.join([str(c) for c in males])}")
# print(f"Females left: {'none' if not females else ', '.join([str(c) for c in females])}")
if females:
    print(f"Females left: {', '.join(str(c) for c in females)}")
else:
    print("Females left: none")