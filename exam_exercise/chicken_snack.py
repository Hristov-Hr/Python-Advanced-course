from collections import deque

money = [int(n) for n in input().split()]
food_prices = deque(int(n) for n in input().split())
eaten_food = 0

while money and food_prices:

    current_amount = money.pop()
    food = food_prices.popleft()

    if current_amount < food:
        continue

    else:
        eaten_food += 1
        if current_amount > food:
            current_amount -= food
            if money:
                money[-1] += current_amount
            else:
                money.append(current_amount)

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")

elif eaten_food > 1:
    print(f"Henry ate: {eaten_food} foods.")
else:
    print("Henry ate: 1 food.") if eaten_food == 1 else print("Henry remained hungry. He will try next weekend again.")
