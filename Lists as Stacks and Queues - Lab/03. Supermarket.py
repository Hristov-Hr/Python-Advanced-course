from collections import deque

my_deque = deque()

while True:
    name = input()

    if name == 'End':
        break
    elif name == 'Paid':
        for i in range(len(my_deque)):
            print(my_deque.popleft())
    else:
        my_deque.append(name)

print(f"{len(my_deque)} people remaining.")