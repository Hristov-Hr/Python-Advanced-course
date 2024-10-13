def accommodate_new_pets(capacity, max_weight, *data):

    accommodated_pets = {}
    result = []

    for pet, weight in data:
        if capacity == 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if weight > max_weight:
            continue
        if pet not in accommodated_pets:
            accommodated_pets[pet] = 0
        accommodated_pets[pet] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for k, v in sorted(accommodated_pets.items()):
        result.append(f"{k}: {v}")

    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
