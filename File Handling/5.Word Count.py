import re

words = []
with open('words.txt') as file:
    words += file.read().split()

text = []
with open('input.txt') as file:
    text += re.findall(r'[A-Za-z\']+', file.read().lower())

result = {}
for word in words:
    if word in text:
        result[word] = text.count(word)

with open('output.txt', 'w') as file:
    for k, v in sorted(result.items(), key=lambda x: -x[1]):
        file.write(f"{k} - {v}\n")
