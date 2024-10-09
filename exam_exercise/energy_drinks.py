from collections import deque

milligrams_caffeine = [int(n) for n in input().split(', ')]
energy_drinks = deque(int(n) for n in input().split(', '))

total_caffeine = 0

while milligrams_caffeine and energy_drinks:
    caffeine = milligrams_caffeine.pop()
    drink = energy_drinks.popleft()
    if caffeine * drink + total_caffeine <= 300:
        total_caffeine += caffeine * drink
    else:
        energy_drinks.append(drink)
        total_caffeine -= 30 if total_caffeine >= 30 else 0

print("At least Stamat wasn't exceeding the maximum caffeine.") if not energy_drinks else \
    print(f"Drinks left: {', '.join(str(n) for n in energy_drinks)}")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")