from HuobiServices import *
import time

def getLowestPrice(symbol):
    k_line = get_kline(symbol, '1min')
    startTimeStamp = k_line['data'][0]['id']
    nowTimeStamp = time.time()
    print(startTimeStamp)
    print(nowTimeStamp)
    return k_line['data'][0]['low']

def getLowestSell(symbol):
    depth = get_depth(symbol)
    val = depth['tick']['asks'][0]
    return val

def getMoney(symbol):
    balance = get_balance()['data']['list']
    for b in balance:
        if b['currency'] == 'btc' and b['type'] == 'trade':
            return float(b['balance'])

    print(balance['data'])

def buy(symbol, price, amount):
    send_order(amount, symbol, 'buy-limit', price)

def cancelAllOrder(symbol):
    orders = orders_list(symbol, 'submitted')['data']
    for order in orders:
        cancel_order(order['id'])

def hasOpen(symbol):
    return 1

if __name__ == "__main__":
    tradeName = 'iostbtc'
    print(getLowestPrice(tradeName))
    print(getLowestSell(tradeName))
    print(getMoney(tradeName))
    print(get_symbols())



