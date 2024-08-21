def calculate_sum_of_coins(coins, amount):

    result = ''
    total_coins = 0

    for value in coins:
        current_coin = amount // value
        amount %= value
        if current_coin > 0:
            result += f"{current_coin} coin(s) with value {value}\n"
            total_coins += current_coin

    if amount > 0:
        return "Error"
    return f"Number of coins to take: {total_coins}\n{result}"


print(calculate_sum_of_coins(sorted([int(i) for i in input().split(', ')], reverse=True), int(input())))