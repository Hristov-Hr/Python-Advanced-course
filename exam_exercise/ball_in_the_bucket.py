def points(c):
    num = 0
    for i in range(SIZE):
        if board[i][c].isdigit():
            num += int(board[i][c])
    return num


SIZE = 6
board = [(input().split()) for _ in range(SIZE)]

NUMBER_OF_SHOOTS = 3

total_points = 0

for _ in range(NUMBER_OF_SHOOTS):
    row, col = [int(n) for n in input().strip("()").split(', ')]

    try:
        target = board[row][col]
        if target == 'B':
            current_points = points(col)
            total_points += current_points
            board[row][col] = '0'

    except IndexError:
        continue

prize = ''
if total_points >= 300:
    prize = 'Lego Construction Set'
elif 200 <= total_points <= 299:
    prize = 'Teddy Bear'
elif 100 <= total_points <= 199:
    prize = 'Football'

print(f"Good job! You scored {total_points} points, and you've won {prize}.") if prize \
    else print(f"Sorry! You need {100 - total_points} points more to win a prize.")