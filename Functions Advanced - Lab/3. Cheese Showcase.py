def sorting_cheeses(**kwargs):

    result = ''
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese in sorted_kwargs:
        result += cheese[0] + '\n'
        for piece in sorted(cheese[1], reverse=True):
            result += str(piece) + '\n'

    return result

