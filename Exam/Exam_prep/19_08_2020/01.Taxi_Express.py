from collections import deque

costumers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]

time = 0

while costumers and taxis:
    costumer = costumers.popleft()
    taxi = taxis.pop()

    if taxi >= costumer:
        time += costumer

    else:
        costumers.appendleft(costumer)

if not costumers:
    print('All customers were driven to their destinations')
    print(f"Total time: {time} minutes")

else:
    print('Not all customers were driven to their destinations')
    x = [str(x) for x in costumers]
    print(f"Customers left: {', '.join(x)}")
