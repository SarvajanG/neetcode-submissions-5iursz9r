class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memoization(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = memoization(i + 1) + memoization(i + 2)
            return cache[i]
        
        return memoization(0)