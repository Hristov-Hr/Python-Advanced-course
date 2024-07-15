from collections import deque

time_for_green_light = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
crash = False
crashed_car = ''
point = 0

while crash is False:
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        time = time_for_green_light
        while cars:
            car = cars.popleft()
            car_length = len(car)
            time -= car_length
            if time > 0:
                passed_cars += 1
                continue
            time += free_window
            if time < 0:
                crash = True
                crashed_car = car
                point = time
            else:
                passed_cars += 1
            break

    else:
        cars.append(command)

if crash:
    print("A crash happened!")
    print(f"{crashed_car} was hit at {crashed_car[point]}.")
else:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")