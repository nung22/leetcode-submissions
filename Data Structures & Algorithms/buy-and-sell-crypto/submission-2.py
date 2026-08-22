class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0, 1
        max_profit = 0


        while fast < len(prices):
            current_profit = prices[fast] - prices[slow]
            max_profit = max(max_profit, current_profit)
            if prices[fast] < prices[slow]:
                slow = fast
            fast += 1
        
        return max_profit