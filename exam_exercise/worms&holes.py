from collections import deque

worms = [int(n) for n in input().split()]
holes = deque(int(n) for n in input().split())
total_worms = len(worms)
matches = 0

while worms and holes:

    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_hole == current_worm:
        matches += 1

    else:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

print(f"Matches: {matches}") if matches > 0 else print("There are no matches.")
print("Every worm found a suitable hole!") if total_worms == matches else print(f"Worms left: {', '.join(str(n) for n in worms) if worms else 'none'}")
print(f"Holes left: {', '.join(str(n) for n in holes) if holes else 'none'}")
