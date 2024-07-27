from collections import deque


def check_index(position, direct):
    if direct == 'left' and position[1] - 1 >= 0:
        position[1] -= 1
    elif direct == 'right' and position[1] + 1 < size:
        position[1] += 1
    elif direct == 'up' and position[0] - 1 >= 0:
        position[0] -= 1
    elif direct == 'down' and position[0] + 1 < size:
        position[0] += 1
    return position


size = int(input())
directions = deque(input().split())
matrix = []
miner_position = []
coal = 0

for i in range(size):
    row = input().split()
    matrix.append(row)
    coal += row.count('c')
    if 's' in row:
        miner_position = [i, row.index('s')]

while directions:
    row, col = check_index(miner_position, directions.popleft())
    if matrix[row][col] == 'c':
        coal -= 1
        matrix[row][col] = '*'
        if coal == 0:
            print(f"You collected all coal! {miner_position[0], miner_position[1]}")
            break
    elif matrix[row][col] == 'e':
        print(f"Game over! {miner_position[0], miner_position[1]}")
        break
else:
    print(f"{coal} pieces of coal left. {miner_position[0], miner_position[1]}")