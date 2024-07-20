guests = set()

for guest in range(int(input())):
    guests.add(input())

command = input()
while command != 'END':
    if command in guests:
        guests.remove(command)
    command = input()

print(len(guests))
for guest in sorted(guests):
    print(guest)