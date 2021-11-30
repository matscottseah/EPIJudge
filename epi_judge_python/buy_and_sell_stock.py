from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    currentMax = 0.0
    buy = sell = 0
    while sell < len(prices):
        diff = prices[sell] - prices[buy]
        if diff < 0:
            buy = sell
        else:
            currentMax = max(diff, currentMax)
            sell += 1
        
    return currentMax


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
