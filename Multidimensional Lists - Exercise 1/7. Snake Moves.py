from collections import deque

rows, columns = [int(n) for n in input().split()]
snake = deque([x for x in input()])

for i in range(rows):
    sub_matrix = ''
    for j in range(columns):
        char = snake.popleft()
        snake.append(char)
        sub_matrix += char
    if i % 2 != 0:
        sub_matrix = sub_matrix[::-1]
    print(sub_matrix)


