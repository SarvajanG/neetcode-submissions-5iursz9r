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
            print(m, curHours)
            if curHours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res