from collections import deque

quantity_of_food = int(input())

orders = deque()

for order in input().split():
    orders.append(int(order))

max_order = max(orders)

for i in range(len(orders)):
    order = orders.popleft()
    if order <= quantity_of_food:
        quantity_of_food -= order
    else:
        orders.appendleft(order)
        break

print(max_order)
if len(orders) == 0:
    print('Orders complete')

else:
    print("Orders left:", ' '.join([str(order) for order in orders]))
