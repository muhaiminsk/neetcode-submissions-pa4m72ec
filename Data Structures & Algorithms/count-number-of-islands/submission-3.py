class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions= [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()
        q = collections.deque()

        def bfs(r,c):
            visit.add((r,c))
            q.append((r,c))
            while q:
                R, C = q.popleft()
                for dr, dc in directions:
                    row, col = R+dr, C+dc
                    if (row in range(ROWS)) and (col in range(COLS)) and grid[row][col] == "1" and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))
                    


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1

        return islands

        