# 200. Number of Islands
# land '1', water '0'
# find out how many island, lands connected horizontally or vertically
# go through the map,
# when find a land, count++
# flip all adjacent lands to water

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # up, down, left, right
        m = len(grid)
        n = len(grid[0])

        # is a valid piece of land
        def is_valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == "1"

        def dfs(i, j):
            if not is_valid(i, j):
                return
            # Flip the land
            grid[i][j] = "0"
            for di, dj in directions:
                dfs(i + di, j + dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count