queries = []

for _ in range(int(input())):
    query = input().split()
    if query[0] == '1':
        queries.append(int(query[1]))
    elif query[0] == '2' and len(queries) > 0:
        queries.pop()
    elif query[0] == '3' and len(queries) > 0:
        print(max(queries))
    elif query[0] == '4' and len(queries) > 0:
        print(min(queries))

queries.reverse()
print(*queries, sep=', ')