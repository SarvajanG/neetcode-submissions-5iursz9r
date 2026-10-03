class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftmax = 0
        rightmax = 0
        res = 0
        while l <= r:
            if leftmax < rightmax:
                if leftmax - height[l] > 0:
                    res += leftmax - height[l]
                leftmax = max(leftmax, height[l])
                l += 1
            else:
                if rightmax - height[r] > 0:
                    res += rightmax - height[r]
                rightmax = max(rightmax, height[r])
                r -= 1
        return res
