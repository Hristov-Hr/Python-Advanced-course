from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = list(int(n) for n in input().split())
locks = deque(int(n) for n in input().split())
value_of_the_intelligence = int(input())

gun_barrel_current_quantity = gun_barrel

while len(bullets) > 0:
    gun_barrel_current_quantity -= 1
    value_of_the_intelligence -= bullet_price
    lock = locks.popleft()
    bullet = bullets.pop()
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)
    if gun_barrel_current_quantity == 0 and len(bullets) > 0:
        print('Reloading!')
        gun_barrel_current_quantity = min(gun_barrel, len(bullets))
    if len(locks) == 0:
        print(f"{len(bullets)} bullets left. Earned ${max(value_of_the_intelligence, 0)}")
        break
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")