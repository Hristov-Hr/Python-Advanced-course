from collections import deque

packages_weight = [int(n) for n in input().split()]
couriers_capacities = deque(int(n) for n in input().split())
total_weight = 0

while packages_weight and couriers_capacities:

    weight = packages_weight.pop()
    capacity = couriers_capacities.popleft()

    if capacity >= weight:
        total_weight += weight
        capacity -= weight * 2
        if capacity > 0:
            couriers_capacities.append(capacity)

    else:
        weight -= capacity
        total_weight += capacity
        packages_weight.append(weight)

print(f"Total weight: {total_weight} kg")
if not packages_weight and not couriers_capacities:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

if packages_weight:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages_weight)}")
if couriers_capacities:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers_capacities)} but there are no more packages to deliver.")



