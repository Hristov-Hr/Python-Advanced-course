first_set = set()
second_set = set()

first_length, second_length = input().split()
for _ in range(int(first_length)):
    first_set.add(int(input()))
for _ in range(int(second_length)):
    second_set.add(int(input()))
for num in first_set & second_set:
    print(num)