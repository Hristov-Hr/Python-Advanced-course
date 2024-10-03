def stock_availability(inventory: list, case_type, *args):

    if case_type == 'delivery':
        [inventory.append(a) for a in args]
    elif case_type == 'sell':
        if not args:
            inventory = inventory[1:]
        elif type(args[0]) is int:
            inventory = inventory[args[0]:]
        else:
            new = []
            for el in inventory:
                if el not in args:
                    new.append(el)
            inventory = new
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

