class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        largest = nums[0]
        curSum = 0
        while r < len(nums):    
            if nums[r] > curSum + nums[r]:
                l = r
                curSum = 0
            curSum += nums[r]
            r += 1
            largest = max(largest, curSum)
        return largest