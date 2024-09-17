SIZE = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for i in range(SIZE):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][SIZE - 1 - i])

print(f"Primary diagonal: {', '.join(str(n) for n in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(n) for n in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
