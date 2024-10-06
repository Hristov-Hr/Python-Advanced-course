from collections import deque

bowls_of_ramen = [int(n) for n in input().split(', ')]
customers = deque(int(n) for n in input().split(', '))

while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()
    if bowl > customer:
        bowls_of_ramen.append(bowl - customer)
    elif customer > bowl:
        customers.appendleft(customer - bowl)
    else:
        continue

print("Great job! You served all the customers.") if not customers else \
    print("Out of ramen! You didn't manage to serve all customers.")
if customers:
    print(f"Customers left: {', '.join(str(n) for n in customers)}")
if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join(str(n) for n in bowls_of_ramen)}")