import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0
        def bfs(r,c):

            q = collections.deque() #f
            q.append((r,c))
            visit.add((r,c))
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    
                    row, col = dr + r, dc + c
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row,col) not in visit:
                        visit.add((row,col))
                        q.append((row,col))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands
        
                