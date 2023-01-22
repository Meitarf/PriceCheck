def price_check(products, product_prices, product_sold, sold_price):
    products_with_prices = dict(zip(products, product_prices))
    sold_products_with_prices = dict(zip(product_sold, sold_price))
    counter = 0
    for key, value in products_with_prices.items():
        if key in sold_products_with_prices and sold_products_with_prices[key] != value:
            counter += 1
    return counter


print(price_check(products=['rice', 'sugar', 'wheat', 'cheese'],
product_prices=[16.89, 56.92, 20.89, 345.99],
product_sold=['rice', 'cheese'],
sold_price=[18.99, 400.89]))
