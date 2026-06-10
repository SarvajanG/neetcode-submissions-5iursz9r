class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def memo(i, curTarget):
            if i == len(nums):
                if curTarget == 0:
                    return 1
                else:
                    return 0
            if (i,curTarget) in cache:
                return cache[(i,curTarget)]
            cache[(i,curTarget)] = memo(i + 1, curTarget - nums[i]) + memo(i + 1, curTarget + nums[i])
            return cache[(i,curTarget)]
        return memo(0, target)