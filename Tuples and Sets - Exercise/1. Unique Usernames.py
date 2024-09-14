names = set()

for _ in range(int(input())):
    names.add(input())

print(*names, sep='\n')

# solution 2 -> set - comprehension
# print(*{input() for _ in range(int(input()))}, sep='\n')