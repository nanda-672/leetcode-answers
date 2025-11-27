class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_price = None
        total_profit = 0
        profit = 0
        for i in range(len(prices)):
            if left_price is None:
                left_price = prices[i]
            if prices[i] < left_price or prices[i] < prices[i-1]:
                left_price = prices[i]
                total_profit += profit
                profit = 0
            else:
                profit = prices[i] - left_price
        total_profit += profit
        return total_profit
        