row, col = [int(i) for i in input().split()]
matrix = [input().split() for _ in range(row)]

command = input()

while command != 'END':

    try:
        r_1, c_1, r_2, c_2 = [int(n) for n in command.split()[1:]]
        try:
            matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
            [print(' '.join(m)) for m in matrix]

        except IndexError:
            print("Invalid input!")

    except ValueError:
        print("Invalid input!")

    command = input()