class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = nums[0]
        while l <= r:
            m = l + (r-l)//2
            print(nums[m], nums[r])
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
            minVal = min(minVal, nums[m])
        return minVal