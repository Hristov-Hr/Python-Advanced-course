def flights(*args):
    destinations = {}

    for i in range(0, len(args), 2):
        if args[i] == 'Finish':
            break
        if args[i] not in destinations:
            destinations[args[i]] = 0

        destinations[args[i]] += args[i + 1]

    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
