rows, columns = [int(n) for n in input().split(', ')]
matrix = []

biggest_values = {}

for _ in range(rows):
    matrix.append([int(n) for n in input().split(', ')])
for i in range(rows - 1):
    for j in range(columns - 1):
        value = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if value not in biggest_values:
            biggest_values[value] = ((matrix[i][j], matrix[i][j + 1]), (matrix[i + 1][j], matrix[i + 1][j + 1]))


for result in biggest_values[max(biggest_values)]:
    print(*result)
print(max(biggest_values))
