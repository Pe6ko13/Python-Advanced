from collections import deque


def flights(*args):
    result = {}
    towns = []
    passengers = deque()
    for i in range(len(args)):
        if i % 2 == 0:
            towns.append(args[i])
        else:
            passengers.append(args[i])

    for town in towns:
        if town == 'Finish':
            break
        if town not in result:
           result[town] = 0
        current_pass = passengers.popleft()
        result[town] += current_pass

    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))