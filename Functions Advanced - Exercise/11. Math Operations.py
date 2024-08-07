from collections import deque


def math_operations(*args, **kwargs):

    operators = {
        'a': lambda a, b: a + b,
        's': lambda a, b: a - b,
        'm': lambda a, b: a * b,
        'd': lambda a, b: a / b
    }

    numbers = deque(args)

    while numbers:
        for k in kwargs:
            if numbers:
                try:
                    kwargs[k] = operators[k](kwargs[k], numbers.popleft())
                except ZeroDivisionError:
                    continue

            else:
                break

    return '\n'.join(f"{i[0]}: {i[1]:.1f}" for i in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
