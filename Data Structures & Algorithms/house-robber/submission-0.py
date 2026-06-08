class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums) - 1
        def memoization(i):
            if i == n:
                return nums[i]
            elif i > n:
                return 0
            elif i in cache:
                return cache[i]
            cache[i] = nums[i] + max(memoization(i + 2), memoization(i + 3))
            return cache[i]
        return max(memoization(0), memoization(1))
