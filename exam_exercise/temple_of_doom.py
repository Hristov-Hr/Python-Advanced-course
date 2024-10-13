from collections import deque

tools = deque(int(n) for n in input().split())
substances = [int(n) for n in input().split()]
challenges = [int(n) for n in input().split()]

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()
    value = tool * substance

    if value in challenges:
        challenges.remove(value)
        continue
    tools.append(tool + 1)
    if substance > 1:
        substances.append(substance - 1)

print("Harry is lost in the temple. Oblivion awaits him.") if challenges else \
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if tools:
    print(f"Tools: {', '.join(str(n) for n in tools)}")
if substances:
    print(f"Substances: {', '.join(str(n) for n in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(n) for n in challenges)}")