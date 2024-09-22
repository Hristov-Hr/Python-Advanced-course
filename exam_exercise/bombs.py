from collections import deque


def bombs(bmb):
    is_ready = True
    for b in bmb.values():
        if b < 3:
            is_ready = False
            break
    return is_ready


bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = list(map(int, input().split(', ')))

bombs_values = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

successfully_bombs = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}

while bomb_effects and bomb_casings and not bombs(successfully_bombs):

    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    value = current_casing + current_effect

    if value in bombs_values:
        bomb_type = bombs_values[value]
        successfully_bombs[bomb_type] += 1
        continue

    bomb_effects.appendleft(current_effect)
    current_casing -= 5
    if current_casing < 0:
        continue
    bomb_casings.append(current_casing)

print("Bene! You have successfully filled the bomb pouch!") if bombs(successfully_bombs) else \
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings) if bomb_casings else 'empty'}")

for k, v in successfully_bombs.items():
    print(f"{k}: {v}")