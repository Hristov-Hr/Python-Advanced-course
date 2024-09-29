from collections import deque

pizza_orders = deque(int(n) for n in input().split(', '))
employees = [int(n) for n in input().split(', ')]

completed_pizzas = 0

while pizza_orders and employees:

    if not 0 < pizza_orders[0] <= 10:
        pizza_orders.popleft()
        continue

    employee = employees.pop()

    if pizza_orders[0] > employee:
        completed_pizzas += employee
        pizza_orders[0] -= employee
        continue

    completed_pizzas += pizza_orders.popleft()

print(f'All orders are successfully completed!\n'
      f'Total pizzas made: {completed_pizzas}') if not pizza_orders else print('Not all orders are completed.')
if employees:
    print(f"Employees: {', '.join(str(e) for e in employees)}")
if pizza_orders:
    print(f"Orders left: {', '.join(str(p) for p in pizza_orders)}")
