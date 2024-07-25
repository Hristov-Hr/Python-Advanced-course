matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            primary_diagonal.append(matrix[i][i])
        if j == len(matrix) - 1 - i:
            secondary_diagonal.append(matrix[i][j])


print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
