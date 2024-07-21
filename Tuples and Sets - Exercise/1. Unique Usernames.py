names = set()

for _ in range(int(input())):
    names.add(input())
for name in names:
    print(name)

# solution 2 -> set - comprehension
# print(*{input() for _ in range(int(input()))}, sep='\n')