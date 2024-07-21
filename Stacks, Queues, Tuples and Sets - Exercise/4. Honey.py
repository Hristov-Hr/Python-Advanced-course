from collections import deque

functions = {
    '-': lambda a, b: abs(a - b),
    '+': lambda a, b: abs(a + b),
    '*': lambda a, b: abs(a * b),
    '/': lambda a, b: abs(a / b) if b != 0 else 0,
}

bees = deque(int(x) for x in input().split())
nectar_values = [int(x) for x in input().split()]
symbols = deque(input().split())
collected_honey = 0

while bees and nectar_values:
    bee = bees.popleft()
    nectar = nectar_values.pop()
    symbol = symbols.popleft()
    if bee > nectar:
        bees.appendleft(bee)
        symbols.appendleft(symbol)
    else:
        honey = functions[symbol](bee, nectar)
        collected_honey += honey

print(f"Total honey made: {collected_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar_values:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_values)}")