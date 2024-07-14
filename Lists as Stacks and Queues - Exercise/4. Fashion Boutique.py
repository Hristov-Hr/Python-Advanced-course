box_of_clothes = list(map(int, input().split()))
capacity_of_rack = int(input())

current_rack = capacity_of_rack
number_of_racks = 1

while box_of_clothes:
    dress = box_of_clothes.pop()
    if current_rack < dress:
        number_of_racks += 1
        current_rack = capacity_of_rack
    current_rack -= dress
print(number_of_racks)