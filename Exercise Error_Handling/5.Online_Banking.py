class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


def send_money(code, total, years, amount, pin_pass):

    if total < amount:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

    if code != pin_pass:
        raise PINCodeError("Invalid PIN code")

    if years < 18:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    total -= amount
    print(f"Successfully sent {amount:.2f} money to a friend"
          f"There is {total:.2f} money left in the bank account")
    return total


def receive_money(amount, total):
    if amount < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    total += amount / 2
    print(f"{amount / 2:.2f} money went straight into the bank account")
    return total


pin_code, balance, age = [int(n) for n in input().split(', ')]


while True:

    command = input().split('#')

    if command[0] == 'End':
        break

    elif command[0] == 'Send Money':
        money, pin = command[1:]
        balance = send_money(pin_code, balance, age, int(money), int(pin))

    elif command[0] == 'Receive Money':
        money = int(command[1])
        balance = receive_money(money, balance)

