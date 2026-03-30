class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]#f

        visit=set()
        islands = 0 #f


        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    row1 = row+dr
                    col1 =col +dc
                    if (row1 in range(rows) and col1 in range(cols) and grid[row1][col1] == "1" and  (row1,col1) not in visit):
                        q.append((row1,col1))
                        visit.add((row1,col1))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands

    


