from collections import defaultdict


class Solution:

    def largest_island(self, grid: list[list[int]]) -> int:
        N = len(grid)

        def out_of_bounds(r, c):
            return r < 0 or c < 0 or r >= N or c >= N

        # DFS and also return the area from (r, c)
        def dfs(r, c, label):
            if (out_of_bounds(r, c) or grid[r][c] == 0 or grid[r][c] == label):
                return 0
            grid[r][c] = label
            size = 1

            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in nei:
                size += dfs(nr, nc, label)
            return size

        def connect(r, c):
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            visited = set()
            # the size of the connecting piece
            result = 1
            # The loop is only 4 times: 4 neighbors
            for nr, nc in nei:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visited:
                    result += size[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            return result

        # 1. Precompute areas
        size = defaultdict(int)  # island label# -> size
        label = 2
        result = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:  # never been labeled
                    size[label] = dfs(r, c, label)
                    label += 1

        # 2. Try flipping water
        # if not size... meaning there is not existing island
        result = 0 if not size else max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    result = max(result, connect(r, c))

        return result
