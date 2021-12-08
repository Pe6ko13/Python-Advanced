from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0
finished = False

while chocolates and cups_of_milk:
    choco = chocolates.pop()
    milk = cups_of_milk.popleft()

    if choco <= 0:
        if milk <= 0:
            continue
        cups_of_milk.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(choco)
        continue

    if milk == choco:
        milkshakes += 1

    if milkshakes == 5:
        finished = True
        break

    if milk != choco:
        cups_of_milk.append(milk)
        chocolates.append(choco - 5)

if finished:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
