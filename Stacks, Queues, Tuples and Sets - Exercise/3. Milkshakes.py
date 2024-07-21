from collections import deque

chocolate_numbers = deque(int(x) for x in input().split(', '))
milk_cups = deque(int(x) for x in input().split(', '))
milkshakes = 0

while milkshakes < 5:
    if not chocolate_numbers or not milk_cups:
        break
    chocolate = chocolate_numbers.pop()
    milk = milk_cups.popleft()
    if chocolate <= 0 or milk <= 0:
        if chocolate > 0:
            chocolate_numbers.append(chocolate)
        if milk > 0:
            milk_cups.appendleft(milk)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolate_numbers.appendleft(chocolate - 5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if len(chocolate_numbers) > 0:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate_numbers)}")
else:
    print('Chocolate: empty')
if len(milk_cups) > 0:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print('Milk: empty')
