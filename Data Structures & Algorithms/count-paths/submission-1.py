class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def memo(row, col, m, n):
            if row >= m or col >= n:
                return 0
            if row == m - 1 or col == n - 1:
                return 1
            if (row, col) in cache:
                return cache[(row,col)]
            cache[(row,col)] = memo(row + 1, col, m, n) + memo(row, col + 1, m, n)
            return cache[(row,col)]
        return memo(0, 0, m, n)