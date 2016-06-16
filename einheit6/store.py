item_prices = {'milk': 1.09, 'bread': 1.99, 'eggs': 3.19}

# return the price a specific product
def get_price(item):
    # check if item exists
    if item in item_prices:
        return item_prices[item]
    else:
        print 'Item not available.'

print get_price('milk')
print get_price('water')
print get_price('bread')
