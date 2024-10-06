from collections import deque

energies = deque(int(n) for n in input().split())
materials = [int(n) for n in input().split()]
elf_counter = 0
toys = 0
total_energy = 0

while energies and materials:
    energy = energies.popleft()
    if energy < 5:
        continue
    elf_counter += 1
    material = materials.pop()
    quantity = 2 if elf_counter % 3 == 0 else 1

    if energy >= material * quantity:
        total_energy += material * quantity
        if elf_counter % 5 == 0:
            energies.append(energy - material * quantity)
            continue
        toys += quantity
        energies.append((energy - material * quantity) + 1)

    else:
        energies.append(energy * 2)
        materials.append(material)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if energies:
    print(f"Elves left: {', '.join(str(s) for s in energies)}")
if materials:
    print(f"Boxes left: {', '.join(str(s) for s in materials)}")


