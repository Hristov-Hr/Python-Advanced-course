cars = set()

for _ in range(int(input())):
    position, car_number = input().split(', ')
    if position == 'IN':
        cars.add(car_number)
    elif position == 'OUT':
        if car_number in cars:
            cars.remove(car_number)

if len(cars) == 0:
    print("Parking Lot is Empty")
else:
    for num in cars:
        print(num)