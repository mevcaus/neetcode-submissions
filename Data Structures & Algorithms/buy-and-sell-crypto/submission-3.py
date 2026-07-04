class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_seen_price = 10000
        for price in prices:
            profit = max(profit, price - lowest_seen_price)
            lowest_seen_price = min(lowest_seen_price, price)
        return profit