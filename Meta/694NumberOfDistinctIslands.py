class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        seen = set()
        unique_islands = set()

        # DFS to find all cells in the current island.
        def dfs(row, col, row_origin, col_origin):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or grid[row][col] == 0:
                return
            seen.add((row, col))
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col, row_origin, col_origin)
            dfs(row - 1, col, row_origin, col_origin)
            dfs(row, col + 1, row_origin, col_origin)
            dfs(row, col - 1, row_origin, col_origin)

        # Repeatedly start DFS's as long as there are islands remaining.
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Init as a normal set and later on cast it into frozenset later
                current_island = set()
                dfs(row, col, row, col)

                if current_island:
                    # you can't add a set into a set since set is mutable and non-hashable
                    # gotta cast a set into a frozenset and add it part of a set
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)
