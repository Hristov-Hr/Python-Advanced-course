rows, columns = [int(x) for x in input().split(', ')]

matrix = []
total_sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    total_sum += sum(matrix[row])

print(total_sum)
print(matrix)
