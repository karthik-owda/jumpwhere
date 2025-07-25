# Best time o buy stock market 
class Solution:  
    def maxProfit(self, prices: list[int]) -> int:  
        left, right, max_profit = 0, 1, 0  
        while right < len(prices):  
            if prices[left] < prices[right]:  
                max_profit = max(max_profit, prices[right] - prices[left])  
            else:  
                left = right  
            right += 1  
        return max_profit  
