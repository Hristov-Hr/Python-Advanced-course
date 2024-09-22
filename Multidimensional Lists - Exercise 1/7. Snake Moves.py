from collections import deque

rows, columns = [int(n) for n in input().split()]
snake = deque([x for x in input()])

for i in range(rows):
    sub_matrix = ''
    for j in range(columns):
        sub_matrix += snake[0]
        snake.rotate(-1)
    if i % 2 != 0:
        sub_matrix = sub_matrix[::-1]
    print(sub_matrix)


