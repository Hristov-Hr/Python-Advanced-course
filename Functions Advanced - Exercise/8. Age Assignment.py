def age_assignment(*names, **ages):

    result = [f"{name} is {ages[key]} years old." for name in names for key in ages.keys() if name.startswith(key)]
    return '\n'.join(sorted(result))


# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
