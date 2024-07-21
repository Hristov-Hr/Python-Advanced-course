from collections import deque

presents_magic_values = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}
crafted_presents = {}

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    magic_level = current_material * current_magic
    for gift, value in presents_magic_values.items():
        if value == magic_level:
            if gift not in crafted_presents:
                crafted_presents[gift] = 0
            crafted_presents[gift] += 1
            break
    else:
        if magic_level < 0:
            materials.append(current_material + current_magic)
        elif magic_level == 0:
            if current_material != 0:
                materials.append(current_material)
            elif current_magic != 0:
                magic.appendleft(current_magic)
        else:
            materials.append(current_material + 15)

if {'Doll', 'Wooden train'}.issubset(crafted_presents) or {'Teddy bear', 'Bicycle'}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for gift, amount in sorted(crafted_presents.items()):
    print(f"{gift}: {amount}")