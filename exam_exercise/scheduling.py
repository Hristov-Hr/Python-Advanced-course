from collections import deque

numbers = deque(int(x) for x in input().split(', '))
idx = int(input())
searched_number = numbers[idx]

cycles = 0

for i in range(len(numbers)):
    if numbers[0] < searched_number or (numbers[0] == searched_number and i <= idx):
        cycles += numbers[0]
    numbers.rotate(-1)

print(cycles)