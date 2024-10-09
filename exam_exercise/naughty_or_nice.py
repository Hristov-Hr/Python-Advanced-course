def naughty_or_nice_list(kids, *args, **kwargs):

    sorted_kids = {'Nice': [], 'Naughty': [], 'Not found': []}

    for arg in args:
        num, type_kid = arg.split('-')
        found_kids = [kid for kid in kids if kid[0] == int(num)]
        if len(found_kids) == 1:
            sorted_kids[type_kid].append(found_kids[0][1])
            kids.remove(found_kids[0])

    for k, v in kwargs.items():
        found_kid = [n for n in kids if n[1] == k]
        if found_kid:
            sorted_kids[v].append(found_kid[0][1])
            kids.remove(found_kid[0])

    for j in kids:
        sorted_kids["Not found"].append(j[1])

    result = []
    for key, value in sorted_kids.items():
        if value:
            result.append(f"{key}: {', '.join(value)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))