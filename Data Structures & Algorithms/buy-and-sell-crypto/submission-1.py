class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxProfit = 0
        while r < len(prices):
            curProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, curProfit)
            if prices[r] < prices[l]:
                l = r
            else:
                r += 1
        return maxProfit