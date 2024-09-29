from collections import deque


def is_valid_value(x):
    return x % 25 != 0 and x > 0


males = [int(n) for n in input().split()]
females = deque(int(n) for n in input().split())

matches = 0

while males and females:

    male = males.pop()
    female = females.popleft()

    if not is_valid_value(male):
        females.appendleft(female)
        continue

    if not is_valid_value(female):
        males.append(male)
        continue

    if male == female:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}\n"
      f"Males left: {', '.join(str(x) for x in males[::-1]) if males else 'none'}\n"
      f"Females left: {', '.join(str(x) for x in females) if females else 'none'}")
