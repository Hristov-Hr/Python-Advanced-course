def recursive_factorial_calculate(num):
    if num == 1:
        return 1
    return num * recursive_factorial_calculate(num - 1)


print(recursive_factorial_calculate(int(input())))