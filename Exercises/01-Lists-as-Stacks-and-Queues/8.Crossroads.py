from collections import deque

green_light = int(input())
free_window = int(input())
car = input()
cars = deque()
crashed = False
all_cars = []

while not car == 'END':
    if car == 'green':
        timer = green_light
        if cars:
            copy = cars.popleft()
            current_car = deque(copy)
            while timer:
                if not current_car:
                    if cars:
                        copy = cars.popleft()
                        current_car = deque(copy)
                    else:
                        break
                current_car.popleft()
                timer -= 1
            if current_car:
                window_timer = free_window
                while window_timer and current_car:
                    current_car.popleft()
                    window_timer -= 1
            if current_car:
                crashed = True
                print('A crash happened!')
                print(f'{copy} was hit at {current_car.popleft()}.')
                break
    else:
        cars.append(car)
        all_cars.append(car)
    car = input()
if not crashed:
    print('Everyone is safe.')
    print(f"{len(all_cars) - len(cars)} total cars passed the crossroads.")
