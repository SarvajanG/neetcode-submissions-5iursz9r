class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, height = stack.pop()
                area = (i - start)*height
                largest = max(largest, area)
            stack.append((start,h))
        
        while stack:
            start, height = stack.pop()
            area = (len(heights) - start)*height
            largest = max(largest, area)
        
        return largest