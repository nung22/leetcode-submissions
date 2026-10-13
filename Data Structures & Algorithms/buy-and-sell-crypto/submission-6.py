class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for R in range(len(prices)):
            max_profit = max(max_profit, prices[R] - lowest)
            if prices[R] < lowest:
                lowest = prices[R]
        return max_profit