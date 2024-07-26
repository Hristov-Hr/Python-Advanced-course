rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
equal_cells = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            equal_cells += 1

print(equal_cells)