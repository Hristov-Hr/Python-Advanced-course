from collections import deque

players = deque(input().split(', '))
matrix = [input().split() for _ in range(6)]
wall = []

while True:
    row, col = [int(n.strip('()')) for n in input().split(', ')]
    player = players[0]

    if player in wall:
        wall.remove(player)

    elif matrix[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == 'T':
        print(f"{player} is out of the game! The winner is {players[1]}.")
        break

    elif matrix[row][col] == 'W':
        wall.append(player)
        print(f"{player} hits a wall and needs to rest.")

    players.rotate(1)