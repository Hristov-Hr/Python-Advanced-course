from collections import deque

quantity_of_water = int(input())
queue_with_people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    queue_with_people.append(name)
while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'refill':
        quantity_of_water += int(command[1])
    else:
        person = queue_with_people.popleft()
        if quantity_of_water >= int(command[0]):
            quantity_of_water -= int(command[0])
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

print(f"{quantity_of_water} liters left")