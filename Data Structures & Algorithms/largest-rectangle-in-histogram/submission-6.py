class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                start, height = stack.pop()
                largest = max(largest, (i-start)*height)
            stack.append((start, h))

        while stack:
            start, height = stack.pop()
            largest = max(largest, (len(heights)-start)*height)
        
        return largest