from HuobiServices import *
import time

def getLowestPrice(symbol):
    k_line = get_kline(symbol, '1min')
    if k_line['data'][0]['count'] > 3:
        return k_line['data'][0]['low']
    else:
        return False

def getLowestSell(symbol):
    depth = get_depth(symbol)
    val = depth['tick']['asks'][0]
    return val

def getMoney(symbol):
    balance = get_balance()['data']['list']
    for b in balance:
        if b['currency'] == 'usdt' and b['type'] == 'trade':
            return float(b['balance'])

    print(balance['data'] + 10)

def buy(symbol, price, amount):
    print("symbol:" + symbol)
    print("price" + ":" + str(price))
    print("amount:" + str(amount))
    send_order(amount, symbol, 'buy-limit', price)

def cancelAllOrder(symbol):
    orders = orders_list(symbol, 'submitted')['data']
    for order in orders:
        cancel_order(order['id'])

def hasOpen(symbol):
    symbols = get_symbols()['data']
    for s in symbols:
        if symbol == s['base-currency'] + s['quote-currency']:
            return True
    return False

def quickBuy(symbol):
    while True:
        if hasOpen(symbol):
            break

    stillMoney = getMoney(symbol)
    while stillMoney > 0.000006510:
        lowPrice = getLowestPrice(symbol)
        if not lowPrice:
            continue
        sellPair = getLowestSell(symbol)
        need = sellPair[0] * sellPair[1]
        print("need" + ":" + str(need))
        print("still" + ":" + str(stillMoney))
        if need < stillMoney:
            buy(symbol, sellPair[0], sellPair[1])
        else:
            amount = round(((stillMoney / sellPair[0]) * 0.95), 2) - 0.01
            print("amount:" + str(amount))
            buy(symbol, sellPair[0], (amount))

        cancelAllOrder(symbol)
        stillMoney = getMoney(symbol)

if __name__ == "__main__":
    tradeName = 'iostusdt'
    # quickBuy(tradeName)
    buy(tradeName, 0.00708, 0.01)


