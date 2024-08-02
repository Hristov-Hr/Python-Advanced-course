def check_valid_index(r_, c_):
    return 0 <= r_ < 5 and 0 <= c_ < 5


def move(self, direction, steps):
    ro = direction[0] * steps + self[0]
    co = direction[1] * steps + self[1]
    if check_valid_index(ro, co) and matrix[ro][co] != 'x':
        return [ro, co]
    else:
        return self


def shoot(self, direction):
    ro, co = self
    while check_valid_index(ro, co):
        if matrix[ro][co] == 'x':
            matrix[ro][co] = '.'
            return [ro, co]
        ro += direction[0]
        co += direction[1]
    else:
        return None


matrix = []
self_position = []
targets = 0
hit_targets = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

for row in range(5):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        self_position = [row, matrix[row].index('A')]
    targets += matrix[row].count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        self_position = move(self_position, directions[command[1]], int(command[2]))

    elif command[0] == 'shoot':
        is_found_target = shoot(self_position, directions[command[1]])
        if is_found_target:
            hit_targets.append(is_found_target)

    if len(hit_targets) == targets:
        break

print(f"Training completed! All {targets} targets hit.") if targets == len(hit_targets) else \
    print(f"Training not completed! {targets - len(hit_targets)} targets left.")

if hit_targets:
    print(*hit_targets, sep='\n')