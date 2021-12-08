from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque([int(bullet) for bullet in input().split(' ')])
locks = deque([int(lock) for lock in input().split(' ')])


int_value = int(input())

costs = 0
local_barrel = barrel_size

while bullets and locks:
    cur_lock = locks.popleft()
    cur_bullet = bullets.pop()
    local_barrel -= 1
    costs -= bullet_price

    if cur_bullet <= cur_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(cur_lock)

    if local_barrel == 0:
        if bullets:
            print("Reloading!")
            local_barrel = barrel_size

if locks and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")

else:
    print(f"{len(bullets)} bullets left. Earned ${int_value + costs}")
