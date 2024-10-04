from collections import deque


def gift_complete(r):
    gift = ''
    if 100 <= r <= 199:
        gift = 'Gemstone'
    elif 200 <= r <= 299:
        gift = 'Porcelain Sculpture'
    elif 300 <= r <= 399:
        gift = 'Gold'
    elif 400 <= r <= 499:
        gift = 'Diamond Jewellery'
    return gift


materials_values = [int(n) for n in input().split()]
magic_level = deque(int(n) for n in input().split())
gifts = {}

while materials_values and magic_level:
    material, magic = materials_values.pop(), magic_level.popleft()
    result = material + magic

    if result < 100 and result % 2 == 0:
        result = material * 2 + magic * 3

    elif result < 100 and result % 2 != 0:
        result *= 2

    elif result >= 500:
        result /= 2

    completed_gift = gift_complete(result)
    if not completed_gift:
        continue

    if completed_gift not in gifts:
        gifts[completed_gift] = 0
    gifts[completed_gift] += 1

print("The wedding presents are made!") if ('Gemstone' in gifts and 'Porcelain Sculpture' in gifts) or \
        ('Gold' in gifts and 'Diamond Jewellery' in gifts) else print("Aladdin does not have enough wedding presents.")

if materials_values:
    print(f"Materials left: {', '.join(str(n) for n in materials_values)}")

if magic_level:
    print(f'Magic left: {", ".join(str(n) for n in magic_level)}')

[print(f"{k}: {v}", sep='\n') for k, v in sorted(gifts.items())]