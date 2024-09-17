SIZE = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for i in range(SIZE):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][SIZE - 1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))