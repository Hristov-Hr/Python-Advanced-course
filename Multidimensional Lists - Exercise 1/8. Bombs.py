matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]
coordinates = [[int(y) for y in x.split(',')] for x in input().split()]

for n in coordinates:
    row, column = n
    value = matrix[row][column]
    if value <= 0:
        continue
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] > 0:
                matrix[r][c] -= value

cells = [n for row in range(len(matrix)) for n in matrix[row] if n > 0]
print(f"Alive cells: {len(cells)}")
print(f"Sum: {sum(cells)}")
[print(*sub) for sub in matrix]
