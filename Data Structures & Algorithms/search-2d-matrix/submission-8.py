class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        targetRow = 0
        while l <= r:
            m = l + (r-l)//2
            if target > matrix[m][len(matrix[0])-1]:
                l += 1
            elif target < matrix[m][0]:
                r -= 1
            else:
                targetRow = m
                break
        
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = l + (r-l)//2
            if target > matrix[targetRow][m]:
                l += 1
            elif target < matrix[targetRow][m]:
                r -= 1
            elif target == matrix[targetRow][m]:
                return True
        return False