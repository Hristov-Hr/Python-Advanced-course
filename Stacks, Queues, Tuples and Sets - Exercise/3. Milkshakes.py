from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milk_cups = deque(int(x) for x in input().split(', '))
milkshakes = 0

while milkshakes < 5:
    if not chocolates or not milk_cups:
        break
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()
    if chocolate <= 0 and milk <= 0:
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_cups) or 'empty'}")
