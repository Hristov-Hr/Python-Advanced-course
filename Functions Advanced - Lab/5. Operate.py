from functools import reduce


def operate(operator, *args):

    operators = {
        '+': reduce(lambda a, b: a + b, args),
        '-': reduce(lambda a, b: a - b, args),
        '*': reduce(lambda a, b: a * b, args),
        '/': reduce(lambda a, b: a / b, args)
    }

    return operators[operator]

