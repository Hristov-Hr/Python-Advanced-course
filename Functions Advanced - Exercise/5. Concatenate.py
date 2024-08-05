def concatenate(*args, **kwargs):

    text = ''.join(args)

    for k in kwargs.keys():
        if k in text:
            text = text.replace(k, kwargs[k])

    return text


# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
