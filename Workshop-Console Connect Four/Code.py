class FullColumnError(Exception):
    pass


def print_matrix(mtr):
    [print(r) for r in mtr]


def check_for_valid_column(col):
    return 1 <= col <= 7


def is_it_available_space(mtr):
    for i in mtr[0]:
        if i == 0:
            break
    else:
        mtr = [[0 for _ in range(7)] for _ in range(6)]

    return mtr


def find_place(mtr, col, num):
    for row in range(5, -1, -1):
        if mtr[row][col] == 0:
            mtr[row][col] = num
            return mtr, row
    raise FullColumnError


def check_direction(mtr, row, col, player, direction):

    counter = 0
    for i in direction:
        r, c = i
        row_, col_ = row, col
        for _ in range(3):
            row_ += r
            col_ += c
            try:
                if mtr[row_][col_] == player:
                    counter += 1
                else:
                    break
            except IndexError:
                break
    return counter


def check_for_winner(mtr, row, col, player):
    directions = {
        'up_down': ((-1, 0), (1, 0)),
        'left_right': ((0, -1), (0, 1)),
        'up_left_down_right': ((-1, -1), (1, 1)),
        'up_right_down_left': ((-1, 1), (1, -1))
    }

    winner_ = 0
    for k, v in directions.items():
        if check_direction(mtr, row, col, player, directions[k]) >= 3:
            winner_ = player
            break

    return winner_


matrix = [[0 for _ in range(7)] for _ in range(6)]
player_1 = input('Player 1, enter your name: ')
player_2 = input('Player 2, enter your name: ')
turn = 1
winner = ''

while not winner:

    matrix = is_it_available_space(matrix)
    player_number = 1 if turn % 2 != 0 else 2

    try:
        selected_column = int(input(f"Player {player_number}, please choose a column: "))
    except ValueError:
        print('Please enter a valid digit!')
        continue

    if not check_for_valid_column(selected_column):
        print("Please enter a valid column")
        continue

    try:
        matrix, row_index = find_place(matrix, selected_column - 1, player_number)

    except FullColumnError:
        print('The column is full! Please enter a column with available space: ')
        continue

    winner = check_for_winner(matrix, row_index, selected_column - 1, player_number)

    print_matrix(matrix)
    turn += 1

print(f"{player_1 if winner == 1 else player_2} is winner!")