from collections import deque


def sorting(**kwargs):
    rooms = []
    for k, v in kwargs.items():
        num = int(k.split("_")[1])
        rooms.append([num, v])
    return sorted(rooms, key=lambda x: (x[1], x[0]))


def accommodate(*args, **kwargs):
    guests = deque(args)
    rooms = sorting(**kwargs)

    guests_without_accommodation = 0
    accommodate_guests = []

    while guests:
        guests_group = guests.popleft()
        if not rooms or guests_group > rooms[-1][1]:
            guests_without_accommodation += guests_group
            continue

        for room in rooms:
            capacity = room[1]
            if capacity >= guests_group:
                accommodate_guests.append([room[0], guests_group])
                rooms.remove(room)
                break

    result = [f"A total of {len(accommodate_guests)} accommodations were completed!" if accommodate_guests \
                      else "No accommodations were completed!"]

    for acc_room in sorted(accommodate_guests, key=lambda x: x[0]):
        result.append(f"<Room {acc_room[0]} accommodates {acc_room[1]} guests>")

    if guests_without_accommodation:
        result.append(f"Guests with no accommodation: {guests_without_accommodation}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result)


