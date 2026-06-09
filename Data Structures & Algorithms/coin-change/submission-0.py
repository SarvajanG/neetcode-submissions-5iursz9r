class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def memo(i):
            if i >= amount:
                return 0
            if i in cache:
                return cache[i]
            minimum = 10000000
            for coin in coins:
                if coin <= amount - i:
                    minimum = min(minimum, memo(i + coin))
            cache[i] = 1 + minimum
            return cache[i]
        res = memo(0)    
        return res if res != 10000001 else -1