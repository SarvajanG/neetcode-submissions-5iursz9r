class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            l = i + 1
            r = len(nums) - 1

            while l < r:
                print(i, l , r)
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                elif threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
     
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
            i += 1
        return res