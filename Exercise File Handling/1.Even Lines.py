import os

path = os.path.join('text.txt')

with open(path) as file:
    lines = file.read().split('\n')

    symbols = ('.', ',', '-', '!', '?')

    for i in range(0, len(lines), 2):
        for symbol in symbols:
            lines[i] = lines[i].replace(symbol, '@')

        print(*lines[i].split()[::-1])

