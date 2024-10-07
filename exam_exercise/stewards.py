from collections import deque

seats = input().split(', ')
first_sequence = deque(int(n) for n in input().split(', '))
second_sequence = deque(int(n) for n in input().split(', '))
rotations = 0
seat_matches = []

while rotations < 10 and len(seat_matches) < 3:
    rotations += 1

    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    letter = chr(first_num + second_num)

    if str(first_num) + letter not in seats and str(second_num) + letter not in seats:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)
    else:
        if str(first_num) + letter in seats:
            seat_matches.append(str(first_num) + letter)
            seats.remove(str(first_num) + letter)
        if str(second_num) + letter in seats:
            seat_matches.append(str(second_num) + letter)
            seats.remove(str(second_num) + letter)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
