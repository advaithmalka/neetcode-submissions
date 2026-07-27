class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100
        maxProfit = 0
        for i, price in enumerate(prices):
            if price < minPrice: minPrice = price
            profit = price - minPrice
            if profit > maxProfit: maxProfit = profit
        
        return maxProfit