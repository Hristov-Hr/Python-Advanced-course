from collections import deque

quantity_food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

for _ in range(len(orders)):
    if orders[0] <= quantity_food:
        order = orders.popleft()
        quantity_food -= order
    else:
        print('Orders left:', end=' ')
        print(*orders)
        break
else:
    print('Orders complete')
