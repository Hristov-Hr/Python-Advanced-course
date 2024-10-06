def naughty_or_nice_list(kids, *args, **kwargs):

    nice_kids = []
    naughty_kids = []
    not_found = []

    for arg in args:
        num, type_kid = arg.split('-')
        found_kids = [kid for kid in kids if kid[0] == int(num)]
        if len(found_kids) == 1:
            if type_kid == 'Nice':
                nice_kids.append(found_kids[0][1])
            elif type_kid == 'Naughty':
                naughty_kids.append(found_kids[0][1])
            kids.remove(found_kids[0])
        else:
            continue

    for k, v in kwargs.items():
        found_kid = [n for n in kids if n[1] == k]
        if found_kid:
            if v == 'Nice':
                nice_kids.append(found_kid[0][1])
            elif v == 'Naughty':
                naughty_kids.append(found_kid[0][1])
            kids.remove(found_kid[0])

    for j in kids:
        not_found.append(j[1])

    result = []
    if nice_kids:
        result.append(f"Nice: {', '.join(n for n in nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(n for n in naughty_kids)}")
    if not_found:
        result.append(f"Not found: {', '.join(n for n in not_found)}")

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
