class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        resRow = 0
        while l <= r:
            m = l + (r-l)//2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                resRow = m
                break
        
        l = 0
        r = len(matrix[resRow]) - 1
        while l <= r:
            m = l + (r-l)//2
            if target < matrix[resRow][m]:
                r = m - 1
            elif target > matrix[resRow][m]:
                l = m + 1
            else:
                return True
        return False