from collections import deque

contenstants = deque(int(n) for n in input().split())
pies = [int(n) for n in input().split()]

while contenstants and pies:
    capacity = contenstants.popleft()
    size = pies.pop()

    if capacity > size:
        contenstants.append(capacity - size)
        continue

    size -= capacity
    if size > 1 or (size == 1 and not pies):
        pies.append(size)
    elif size == 1 and pies:
        pies[-1] += size

if contenstants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contenstants)}")

if pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")

if not contenstants and not pies:
    print("We have a champion!")




