numbers = input().split()

counter = {}

for num in numbers:
    if num not in counter:
        counter[num] = numbers.count(num)
for k, v in counter.items():
    print(f"{float(k)} - {v} times")