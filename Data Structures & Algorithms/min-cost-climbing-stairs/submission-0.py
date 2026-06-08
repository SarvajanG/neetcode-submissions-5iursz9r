class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost) - 1
        def memoization(i):
            if i == n:
                return cost[i]
            elif i > n:
                return 0
            elif i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(memoization(i + 1), memoization(i + 2))
            return cache[i]

        return min(memoization(0), memoization(1))