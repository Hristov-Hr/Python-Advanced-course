def even_odd(*args):

    numbers = []

    for num in args:
        if num == 'even':
            return [*filter(lambda x: x % 2 == 0, numbers)]
        elif num == 'odd':
            return [*filter(lambda x: x % 2 != 0, numbers)]
        else:
            numbers.append(int(num))


