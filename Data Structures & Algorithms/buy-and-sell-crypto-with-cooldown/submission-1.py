class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def memo(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in cache:
                return cache[(i,buying)]
            if buying:
                cache[(i,buying)] = max(memo(i+1, False)-prices[i], memo(i+1, True))
            else:
                cache[(i,buying)] = max(memo(i+2, True)+prices[i], memo(i+1, False))
            return cache[(i,buying)]
        return memo(0, True)