def calculate(text):

    num_one, sign, num_two = text.split()

    operators = {
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '^': lambda x, y: x ** y,
    }
    if sign == '/' and num_two == 0:
        return "Can not divide by 0"

    return f"{operators[sign](float(num_one), int(num_two)):.2f}"