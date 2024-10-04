def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    result = ""
    product = 0

    for k, v in kwargs.items():
        price = v[0] * v[1]
        if price > budget:
            continue
        result += f"You bought {k} for {price:.2f} leva." + '\n'
        budget -= price
        product += 1
        if product >= 5:
            break

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
