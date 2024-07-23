rows = int(input())
flatted = []

for _ in range(rows):
    row = input().split(', ')
    for n in row:
        flatted.append(int(n))

print(flatted)
