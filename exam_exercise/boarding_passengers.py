def boarding_passengers(capacity, *args):
    passengers_groups = {}
    is_accommodated = True

    for number, benefits in args:
        if number > capacity:
            is_accommodated = False
            continue
        if benefits not in passengers_groups:
            passengers_groups[benefits] = 0
        passengers_groups[benefits] += number
        capacity -= number

    result = ["Boarding details by benefit plan:"]
    for k, v in sorted(passengers_groups.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"## {k}: {v} guests")
    if is_accommodated:
        result.append("All passengers are successfully boarded!")
    else:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.") if capacity == 0 else result.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
