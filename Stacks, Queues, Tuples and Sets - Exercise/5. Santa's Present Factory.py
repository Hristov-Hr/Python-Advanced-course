from collections import deque


presents_values = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = {}

materials_values = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())

while magic_values and materials_values:

    material = materials_values.pop()
    magic = magic_values.popleft()
    if magic == 0 or material == 0:
        if magic != 0:
            magic_values.appendleft(magic)
        if material != 0:
            materials_values.append(material)
        continue

    magic_level = magic * material
    present = presents_values.get(magic_level, None)

    if present:
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1
        continue

    material += magic if magic_level < 0 else 15
    materials_values.append(material)


if {"Wooden train", "Doll"}.issubset(crafted_presents) or {'Teddy bear', 'Bicycle'}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

print(f"Materials left: {', '.join(str(x) for x in reversed(materials_values))}") if materials_values else None
print(f"Magic left: {', '.join(str(x) for x in magic_values)}") if magic_values else None
[print(f"{k}: {v}") for k, v in sorted(crafted_presents.items())]