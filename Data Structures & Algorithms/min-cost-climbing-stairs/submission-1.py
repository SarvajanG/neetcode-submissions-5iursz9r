class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(i):
            if i == len(cost) - 1:
                return cost[i]
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = min(cost[i] + dp(i + 1), cost[i] + dp(i + 2))
            return cache[i]
        return min(dp(0),dp(1))