class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,  1
        maximum = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maximum = max(maximum, profit)
            else:
                buy = sell
            sell += 1
        return maximum