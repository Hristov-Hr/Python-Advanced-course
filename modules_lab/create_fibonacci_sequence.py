def create_sequence(num):
    sequence = [0, 1]

    while len(sequence) < num:
        new_num = sequence[-1] + sequence[-2]
        sequence.append(new_num)

    return sequence[:num]


def found_number(lst, num):

    try:
        return f"The number - {num} is at index {lst.index(num)}"
    except ValueError:
        return f"The number {num} is not in the sequence"