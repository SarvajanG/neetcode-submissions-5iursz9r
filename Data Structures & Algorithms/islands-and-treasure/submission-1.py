class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dist = 0
        while q:
            dist += 1
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] == 2147483647:
                        q.append((nr,nc))
                        grid[nr][nc] = dist
                