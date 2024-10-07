def shopping_cart(*args):
    limit_for_products = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    products = {"Soup": [], "Pizza": [], "Dessert": []}

    for a in args:
        if a == 'Stop':
            break
        meal, product = a
        if limit_for_products[meal] > 0 and product not in products[meal]:
            products[meal].append(product)
            limit_for_products[meal] -= 1

    sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    if len(sorted_products[0][1]) == 0:
        result.append("No products in the cart!")
    else:
        for k, v in sorted_products:
            result.append(f"{k}:")
            [result.append(f" - {j}") for j in sorted(v)]

    return '\n'.join(result)





print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
