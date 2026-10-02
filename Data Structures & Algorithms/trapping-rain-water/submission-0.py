class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        res = 0

        maxleft = 0
        for i in range(len(height)):
            leftmax[i] = maxleft
            maxleft = max(maxleft, height[i])

        maxright = 0
        for i in range(len(height)-1, -1, -1):
            rightmax[i] = maxright
            maxright = max(maxright, height[i])
 
        for i in range(len(height)):
            water = min(leftmax[i], rightmax[i]) - height[i]
            if water > 0:
                res += water
        return res
