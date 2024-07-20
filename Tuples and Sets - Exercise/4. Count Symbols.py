text = input()
chars_counter = {}

for char in text:
    chars_counter[char] = text.count(char)

for n in sorted(chars_counter.items()):
    print(f"{n[0]}: {n[1]} time/s")