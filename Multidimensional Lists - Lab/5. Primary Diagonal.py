matrix_size = int(input())
total = 0

for i in range(matrix_size):
    total += [int(x) for x in input().split()][i]

print(total)