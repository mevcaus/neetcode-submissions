class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_price = 1000
        for price in prices:
            profit = max(profit, price - lowest_price)
            lowest_price = min(lowest_price, price)
        return profit