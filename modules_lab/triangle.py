def print_triangle(number):
    for row in range(1, number + 1):
        for col in range(row):
            print(col + 1, end=' ')
        print()

    for row in range(number - 1, 0, -1):
        for col in range(row):
            print(col + 1, end=' ')
        print()