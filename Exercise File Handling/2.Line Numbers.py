import os
from string import punctuation

path = os.path.join('text.txt')

with open(path) as file:
    rows = file.readlines()
    for line in range(len(rows)):
        letters = len([x for x in rows[line] if x.isalpha()])
        marks = len([x for x in rows[line] if x in punctuation])
        with open('output_file.txt', 'a') as output_file:
            output_file.write(f"Line {line + 1}: {rows[line].strip()} ({letters})({marks})\n")
