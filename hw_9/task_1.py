coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def diction(key: tuple, value: tuple):
    dictionary = {i: item for i, item in zip(key, value)}
    return dictionary


print(diction(coin, code))

# dictionary = dict(zip(coin, code))
# print(dictionary)
