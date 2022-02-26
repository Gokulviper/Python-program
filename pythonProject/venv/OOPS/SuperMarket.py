class SuperMarket:
    '''
    this is super market
    '''



bread=SuperMarket()
bread.brand='mikbikes'
bread.price=213
biscuit=SuperMarket()
biscuit.price=23
biscuit.brand='halala'

print(biscuit.brand)
print(biscuit.__dict__)#{'price': 23, 'brand': 'halala'}
