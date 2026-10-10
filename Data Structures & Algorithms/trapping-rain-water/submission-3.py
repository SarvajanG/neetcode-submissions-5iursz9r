class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        leftMax, rightMax = 0,0
        while l <= r:
            if leftMax < rightMax:
                cur = leftMax - height[l]
                if cur > 0:
                    res += cur 
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                cur = rightMax - height[r]
                if cur > 0:
                    res += cur
                rightMax = max(rightMax, height[r])
                r -= 1
        return res