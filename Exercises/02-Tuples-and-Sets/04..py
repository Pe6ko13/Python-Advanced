n = int(input())

cars = set()

for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        cars.add(number)
    else:
        if number in cars:
            cars.remove(number)

    # operations = {
    #     'IN': cars.add,
    #     'OUT': cars.remove,
    # }

    # else:
    #     cars.discard(number)      -    remove cars even there isn't cars without bugging the program!

if not cars:
    print('Parking Lot is Empty')
else:
    [print(car) for car in cars]