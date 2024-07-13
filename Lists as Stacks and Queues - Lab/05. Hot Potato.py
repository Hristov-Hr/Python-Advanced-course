from collections import deque

names = deque(input().split())
length_of_step = int(input()) - 1

while len(names) > 1:
    names.rotate(-length_of_step)
    print(f"Removed {names.popleft()}")
print(f"Last is {names.popleft()}")