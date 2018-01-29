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

def buyAll(symbol):
    balance = get_balance()
    print(balance)

if __name__ == "__main__":
    tradeName = 'eosbtc'
    print(getLowestPrice(tradeName))
    print(getLowestSell(tradeName))
    buyAll(tradeName)


