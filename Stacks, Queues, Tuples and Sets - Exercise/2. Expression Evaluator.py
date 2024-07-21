from collections import deque

numbers = deque()
result = None

for x in input().split():
    if x not in '+-*/':
        numbers.append(int(x))
        continue
    if result is None:
        result = numbers.popleft()
    for num in numbers:
        if x == "+":
            result += num
        elif x == "-":
            result -= num
        elif x == '*':
            result *= num
        elif x == "/":
            result //= num
    numbers.clear()
print(result)
