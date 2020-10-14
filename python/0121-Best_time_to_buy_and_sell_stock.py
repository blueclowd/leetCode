'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        min_price = float('inf')
        min_prices = []

        for price in prices:

            if price < min_price:
                min_price = price

            min_prices.append(min_price)

        max_price = -1
        max_prices = []

        for price in reversed(prices):

            if price > max_price:
                max_price = price

            max_prices.append(max_price)

        max_prices = list(reversed(max_prices))
        max_difference = -1

        for min_price, max_price in zip(min_prices, max_prices):

            difference = max_price - min_price

            if difference > max_difference:
                max_difference = difference

        return max_difference
