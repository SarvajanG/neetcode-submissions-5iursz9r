class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        longest = 0
        for i in range(len(nums)):
            curLongest = 0
            if nums[i] - 1 not in checker:
                while nums[i] + curLongest in checker:
                    curLongest += 1
                longest = max(longest, curLongest)
        return longest