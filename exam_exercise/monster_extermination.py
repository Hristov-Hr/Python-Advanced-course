from collections import deque

armor_values = deque(int(n) for n in input().split(','))
impact_values = [int(n) for n in input().split(',')]
killed_monsters = 0

while armor_values and impact_values:
    armor = armor_values.popleft()
    strike_strength = impact_values.pop()
    if strike_strength >= armor:
        killed_monsters += 1
        strike_strength -= armor
        if strike_strength == 0:
            continue
        if impact_values:
            impact_values[-1] += strike_strength
        else:
            impact_values.append(strike_strength)
    else:
        armor -= strike_strength
        armor_values.append(armor)

if not armor_values:
    print("All monsters have been killed!")
if not impact_values:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")