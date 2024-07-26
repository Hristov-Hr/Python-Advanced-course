rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float('-inf')
square = []
for i in range(rows - 2):
    for j in range(columns - 2):
        first_row = matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]              # first_row = matrix[i][j: j + 3]
        second_row = matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2] # second_row = matrix[i + 1][j: j + 3]
        third_row = matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]  # third_row = matrix[i + 2][j: j + 3]
        current_amount = sum(first_row) + sum(second_row) + sum(third_row)
        if current_amount > max_sum:
            max_sum = current_amount
            square = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for squ in square:
    print(*squ)           # [print(*squ) for squ in square]
