from collections import deque

from printy import printy
from pyfiglet import Figlet


def print_initial_board():
    printy(f"This is the numeration of the board:", 'y')
    [printy(f"| {' | '.join(row)} |", 'gB') for row in board]
    for r in range(SIZE):
        for c in range(SIZE):
            board[r][c] = ' '


def error():
    printy('Invalid number. Please select a free space between 1-9 !', 'r')


def check_for_valid_position(pos, r, c):
    return 1 <= pos <= 9 and board[r][c] == ' '


def check_for_winner():
    first_diagonal = all([board[i][i] == players[0][1] for i in range(SIZE)])
    second_diagonal = all([board[i][SIZE - 1 - i] == players[0][1] for i in range(SIZE)])
    all_rows = any(all(x == players[0][1] for x in row) for row in board)
    all_columns = any(all(row[i] == players[0][1] for row in board) for i in range(SIZE))

    return any(x for x in [first_diagonal, second_diagonal, all_rows, all_columns])


def choose_position():
    global turns

    while True:
        position = input(f"{players[0][0]} choose a free position[1-9]: ")
        try:
            position = int(position)
        except ValueError:
            error()
            continue

        pos_row = (position - 1) // SIZE
        pos_col = (position - 1) % SIZE

        if not check_for_valid_position(position, pos_row, pos_col):
            error()
            continue

        turns += 1
        board[pos_row][pos_col] = players[0][1]
        print_board()

        if check_for_winner():
            printy(f"Congratulations, {players[0][0]}. You won!", 'mB')
            raise SystemExit

        if turns == SIZE * SIZE:
            printy('Draw !', "yBU")
            raise SystemExit

        players.rotate()


def print_board():
    [printy(f"| {' | '.join(row)} |", 'wB') for row in board]


def start_game():

    f = Figlet(font='slant')
    printy(f.renderText("Welcome to Tic-Tac-Toe!"), "yB")

    player_one_name = input('Player one, please enter your name: ').capitalize()
    player_two_name = input('Player two, please enter your name: ').capitalize()

    while True:

        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O': ").upper()
        if player_one_symbol not in ['X', 'O']:
            printy(f"{player_one_name}, please select valid option!", 'r')
        else:
            printy(f"{player_one_name}, you selected '{player_one_symbol}'", 'nB')
            player_two_symbol = 'X' if player_one_symbol == 'O' else 'O'
            printy(f"{player_two_name}, you play with '{player_two_symbol}'", 'nB')
            print_initial_board()
            break
    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    choose_position()


SIZE = 3
players = deque()
turns = 0
board = [[str(row + col) for col in range(SIZE)] for row in range(1, SIZE * SIZE + 1, 3)]

start_game()
