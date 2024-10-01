from collections import deque

fireworks_effects = deque(int(n) for n in input().split(', '))
explosive_power = [int(n) for n in input().split(', ')]

successfully_prepared_fireworks = {
        "Palm Fireworks": 0,
        "Willow Fireworks": 0,
        "Crossette Fireworks": 0
}
task_is_complete = False

while fireworks_effects and explosive_power and not task_is_complete:

    current_effect = fireworks_effects.popleft()
    current_power = explosive_power.pop()

    if current_effect <= 0 or current_power <= 0:
        if current_effect > 0:
            fireworks_effects.appendleft(current_effect)
        if current_power > 0:
            explosive_power.append(current_power)
        continue

    mixed_value = current_effect + current_power

    if mixed_value % 3 == 0 and mixed_value % 5 != 0:
        successfully_prepared_fireworks["Palm Fireworks"] += 1
    elif mixed_value % 3 != 0 and mixed_value % 5 == 0:
        successfully_prepared_fireworks["Willow Fireworks"] += 1
    elif mixed_value % 3 == 0 and mixed_value % 5 == 0:
        successfully_prepared_fireworks["Crossette Fireworks"] += 1
    else:
        fireworks_effects.append(current_effect - 1)
        explosive_power.append(current_power)

    if all(x >= 3 for x in successfully_prepared_fireworks.values()):
        task_is_complete = True

print("Congrats! You made the perfect firework show!") if task_is_complete else \
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(f) for f in fireworks_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(e) for e in explosive_power)}")

[print(f"{k}: {v}") for k, v in successfully_prepared_fireworks.items()]