class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = float("inf")
        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
                pass
            if prices[i] - lowest_price > max_profit:
                max_profit =  prices[i] - lowest_price
        return max_profit       