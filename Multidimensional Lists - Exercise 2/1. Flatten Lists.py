matrix = []

for i in input().split('|'):
    sub = []
    for j in i.split():
        sub.append(j)
    if sub:
        matrix.insert(0, sub)

[print(*x, end=' ') for x in matrix]