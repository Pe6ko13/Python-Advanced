from collections import deque

orders_list = [int(el) for el in input().split(', ')]
employee_capacity = [int(x) for x in input().split(', ')]
orders = deque()
pizzas = 0

for order in orders_list:
    if 0 < order < 11:
        orders.append(order)

while employee_capacity and orders:
    current_empl = employee_capacity.pop()
    current_order = orders.popleft()
    if current_empl >= current_order:
        pizzas += current_order
    else:
        current_order -= current_empl
        orders.appendleft(current_order)
        pizzas += current_empl



if not orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employee_capacity])}")

elif not employee_capacity and len(orders) > 0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")