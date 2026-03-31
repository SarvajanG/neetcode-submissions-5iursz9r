class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curWater = (r-l)*min(heights[l], heights[r])
            maxWater = max(maxWater, curWater)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return maxWater