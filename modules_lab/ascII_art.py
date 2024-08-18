from printy import printy
from pyfiglet import figlet_format


def print_message(msg):

    result = figlet_format(msg)
    printy(result, 'mB')


print_message(input())


