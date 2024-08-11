import os


path = os.path.join('numbers.txt')

file = open(path)

# Solution 1:
total = sum([int(line[:-1]) for line in file.readlines()])

# Solution 2:
# total = sum([int(n) for n in file.read() if n.isdigit()])

print(total)