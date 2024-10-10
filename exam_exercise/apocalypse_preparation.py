from collections import deque

textiles = deque(int(n) for n in input().split())
medicaments = [int(n) for n in input().split()]
healing_items = {100: 'MedKit', 40: 'Bandage', 30: 'Patch'}
completed_items = {}

while textiles and medicaments:
    medicament = medicaments.pop()
    value = textiles.popleft() + medicament

    if value > 100:
        medicaments[-1] += value - 100
        value = 100

    if value in healing_items:
        item = healing_items[value]
        if item not in completed_items:
            completed_items[item] = 0
        completed_items[item] += 1

    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    print("Textiles are empty.") if medicaments else print("Medicaments are empty.")

for k, v in sorted(completed_items.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k} - {v}")
if medicaments:
    print(f"Medicaments left: {', '.join(str(m) for m in medicaments[::-1])}")
if textiles:
    print(f"Textiles left: {', '.join(str(t) for t in textiles)}")