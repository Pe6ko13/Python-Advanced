from _collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s =0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m, s


robot = input().split(";")
robots = deque()
busy_robots = deque()
products = deque()
robots_dic = {}
time = [int(x) for x in input().split(':')]

product = input()

while product != 'End':
    products.append(product)


    product = input()

for robo in robot:
    robot_name = robo.split('-')[0]
    robot_time = int(robo.split('-')[1])
    robots.append([robot_name, robot_time])
    robots_dic[robot_name] = robot_time

while products:
    for robo in busy_robots:
        robot_name = robo[0]

        robo[1] -= -1
        if robo[1] <= 0:
            robots.append([robot_name, robots_dic[robot_name]])
    busy_robots = [r for r in busy_robots if r[1] > 0]

    time = next_second(time[0], time[1], time[2])
    current_product = products.popleft()
    if not robots:
        products.append(current_product)
        continue

    current_robot = robots.popleft()
    print(f"{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
    busy_robots.append(current_robot)


# from datetime import datetime, timedelta
#
# time = datetime.strptime(input(), '%H:%M:%S')
# time = time + timedelta(seconds=1)