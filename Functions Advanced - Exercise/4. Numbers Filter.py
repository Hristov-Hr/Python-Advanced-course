def even_odd_filter(**kwargs):
    filters = {
        'even': lambda x: x % 2 == 0,
        'odd': lambda x: x % 2 != 0
    }

    for k, v in kwargs.items():
        kwargs[k] = [*filter(filters[k], v)]
    print(kwargs)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
