class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        direction  = [(1,0),(0,1),(-1,0),(0,-1)]
        def valid (i,j):
            return 0 <= i < row and 0 <= j < col
        def dfs(i,j):
            if not valid(i,j) or grid[i][j] == 0:
                return 0
            total = grid[i][j]
            grid[i][j] = 0

            for dx,dy in direction:
                new_x = dx + i
                new_y = dy + j
                total += dfs(new_x,new_y)
            return total
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    result = max(result,dfs(i,j))
        return result
        