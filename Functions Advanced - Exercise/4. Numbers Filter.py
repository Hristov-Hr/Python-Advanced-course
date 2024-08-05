def even_odd_filter(**kwargs):
    filters = {
        'even': lambda x: x % 2 == 0,
        'odd': lambda x: x % 2 != 0
    }

    result = {}

    for k, v in kwargs.items():
        kwargs[k] = [*filter(filters[k], v)]

    kwargs = sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True)

    for el in kwargs:
        result[el[0]] = el[1]

    return result


# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))

