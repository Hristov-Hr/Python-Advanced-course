def words_sorting(*args):
    words = {}
    total = 0

    for a in args:
        amount = sum(ord(x) for x in a)
        total += amount
        words[a] = amount

    sorted_words = sorted(words.items()) if total % 2 == 0 else sorted(words.items(), key=lambda x: -x[1])
    result = [(f"{k} - {v}") for k, v in sorted_words]

    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
