from collections import deque

cups = deque(int(n) for n in input().split())
bottles = list(int(n) for n in input().split())
wasted_water = 0

while bottles and cups:
    water = bottles.pop() - cups.popleft()
    if water >= 0:
        wasted_water += water
    else:
        cups.appendleft(abs(water))

if not cups:
    print("Bottles:", *bottles)
else:
    print("Cups:", *cups)
print(f"Wasted litters of water: {wasted_water}")