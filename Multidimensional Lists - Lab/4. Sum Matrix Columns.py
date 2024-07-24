rows, columns = input().split(', ')
matrix = [0 for _ in range(int(columns))]

for _ in range(int(rows)):
    sublist = [int(x) for x in input().split()]
    for j in range(int(columns)):
        matrix[j] += sublist[j]
print(*matrix, sep='\n')