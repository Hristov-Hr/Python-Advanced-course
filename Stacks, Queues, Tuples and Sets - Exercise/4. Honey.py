from collections import deque


def honey_making_process(bee_, ntr, sym):

    calc = {
        "-": lambda x, y: x - y,
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else 0
    }

    return abs(calc[sym](bee_, ntr))


bees = deque(int(x) for x in input().split())
nectar_values = deque(int(x) for x in input().split())
symbols = deque(input().split())
honey = 0

while bees and nectar_values:

    bee = bees.popleft()
    nectar = nectar_values.pop()

    if bee > nectar:
        bees.appendleft(bee)
        continue

    honey += honey_making_process(bee, nectar, symbols.popleft())

print(f"Total honey made: {honey}")
print(f"Bees left: {', '.join(str(x) for x in bees)}") if bees else None
print(f"Nectar left: {', '.join(str(x) for x in nectar_values)}") if nectar_values else None