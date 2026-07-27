class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minNum = 101
        for num in prices:
            minNum = min(minNum, num)
            profit = max(profit, num - minNum)

        return profit
