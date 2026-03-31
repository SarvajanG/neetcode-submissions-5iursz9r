class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = l + (r-l)//2
            curHours = 0
            for p in piles:
                curHours += math.ceil(p/k)
            if curHours > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
        return res