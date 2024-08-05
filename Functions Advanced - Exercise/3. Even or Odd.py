def even_odd(*args):

    numbers = []

    for num in args:
        if num == 'even':
            return [*filter(lambda x: x % 2 == 0, numbers)]
        elif num == 'odd':
            return [*filter(lambda x: x % 2 != 0, numbers)]
        else:
            numbers.append(int(num))


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
