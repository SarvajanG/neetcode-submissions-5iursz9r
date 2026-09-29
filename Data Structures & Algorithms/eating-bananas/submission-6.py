class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = r
        while l <= r:
            k = l + (r-l)//2
            curTime = 0
            for p in piles:
                curTime += math.ceil(p/k)
            print(k, curTime)
            if curTime > h:
                l = k + 1
            else:
                minK = min(minK, k)
                r = k - 1
        return minK