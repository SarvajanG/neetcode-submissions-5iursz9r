class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = minK = max(piles)
        
        while l <= r:
            k = l + (r-l)//2
            curHours = 0
            for p in piles:
                curHours += math.ceil(p/k)
            if curHours > h:
                l = k + 1
            else:
                r = k - 1
                minK = min(minK, k)
        return minK
