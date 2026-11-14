class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, curSum):
            if i >= len(nums) or curSum > target:
                return
            elif curSum == target:
                res.append(tuple(subset.copy()))
            
            subset.append(nums[i])
            dfs(i, curSum + nums[i])
            subset.pop()
            dfs(i + 1, curSum)
        dfs(0, 0)
        res2 = []
        for item in set(res):
            res2.append(list(item))
        return res2