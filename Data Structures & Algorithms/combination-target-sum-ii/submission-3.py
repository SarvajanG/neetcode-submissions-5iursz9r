class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()
        def backtrack(i, curSum):
            if curSum == target:
                result.append(subset.copy())
                return
            if i >= len(candidates) or curSum > target:
                return
            subset.append(candidates[i])
            backtrack(i + 1, curSum + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curSum)
        backtrack(0,0)
        return result