class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def infect(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            res = 1
            grid[i][j] = 2
            res += infect(grid, i+1, j)
            res += infect(grid, i, j+1)
            res += infect(grid, i-1, j)
            res += infect(grid, i, j-1)
            return res
        if grid is None:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    square = infect(grid, i, j)
                    res = max(res, square)
        return res
