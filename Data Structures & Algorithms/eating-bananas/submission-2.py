class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = l + (r-l)//2
            curHours = 0
            for p in piles:
                curHours += math.ceil(p/m)
            if curHours <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
            
        return res