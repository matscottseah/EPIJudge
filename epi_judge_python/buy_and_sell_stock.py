from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    minVal, currentMax = float('inf'), 0.0
    for price in prices:
        diff = price - minVal
        currentMax = max(currentMax, diff)
        minVal = min(minVal, price)
        
    return currentMax


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
