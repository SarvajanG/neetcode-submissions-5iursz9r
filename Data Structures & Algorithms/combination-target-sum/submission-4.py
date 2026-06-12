class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(i, curSum):
            if i >= len(nums) or curSum > target:
                return
            if curSum == target:
                result.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i, curSum + nums[i])

            subset.pop()
            backtrack(i + 1, curSum)
        backtrack(0,0)
        return result