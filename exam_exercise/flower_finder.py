from collections import deque

vowels = deque(input().split())
consonants = input().split()
flowers = ['rose', 'tulip', 'lotus', 'daffodil']
flowers_as_set = [set(flower) for flower in flowers]
found_word = -1


while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    letters = {vowel, consonant}

    for i in range(len(flowers_as_set)):
        flowers_as_set[i] = flowers_as_set[i].difference(letters)
        if len(flowers_as_set[i]) == 0:
            found_word = i
            break

    if found_word >= 0:
        found_word = flowers[found_word]
        break

print("Cannot find any word!") if type(found_word) == int else print(f"Word found: {found_word}")
if vowels:
    print(f"Vowels left: {' '.join(l for l in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(l for l in consonants)}")