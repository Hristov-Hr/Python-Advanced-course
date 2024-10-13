from collections import deque

fuel_sequence = [int(n) for n in input().split()]
consumption_indexes = deque(int(n) for n in input().split())
needed_quantities = deque(int(n) for n in input().split())
counter = 0

while fuel_sequence and consumption_indexes and needed_quantities:

    counter += 1
    fuel = fuel_sequence.pop()
    consumption = consumption_indexes.popleft()
    if fuel - consumption >= needed_quantities[0]:
        needed_quantities.popleft()
        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter}")
        break

if not needed_quantities:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    counter -= 1
    if counter == 0:
        print("John didn't reach any altitude.")
    else:
        altitudes = [f"Altitude {n}" for n in range(1, counter + 1)]
        print(f"Reached altitudes: {', '.join(altitudes)}")
