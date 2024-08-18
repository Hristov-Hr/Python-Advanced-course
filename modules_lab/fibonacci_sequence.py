from create_fibonacci_sequence import create_sequence, found_number


command = input()
sequence = []

while command != 'Stop':

    number = int(command.split()[-1])
    if command.startswith('Create'):
        sequence_length = int(command.split()[-1])
        sequence = create_sequence(number)
        print(*sequence)

    elif command.startswith('Locate'):
        print(found_number(sequence, number))

    command = input()