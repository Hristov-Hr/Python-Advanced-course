from collections import deque

number_of_pumps = int(input())
circle = deque()

for _ in range(number_of_pumps):
    petrol, distance = input().split()
    circle.append(int(petrol) - int(distance))

start_index = 0
while True:
    circle_ = circle.copy()
    current_amount = 0
    for _ in range(len(circle_)):
        current_amount += circle_.popleft()
        if current_amount < 0:
            break
    if current_amount >= 0:
        break
    else:
        circle.rotate(-1)
        start_index += 1
print(start_index)