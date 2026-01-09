from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        # Check that the first and last cells are open.
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # helper function to get neighbors that are (0, 0)
        def get_neighbors(row, col):
            for i, j in directions:
                new_row = row + i
                new_col = col + j

                if new_row < 0 or new_row > max_row or new_col < 0 or new_col > max_col:
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        # Set up the BFS.
        queue = deque([(0, 0)])
        grid[0][0] = 1

        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            # if (row, col) == (max_row, max_col):
            if row == max_row and col == max_col:
                return distance
            for neighbour_row, neighbour_col in get_neighbors(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))

        # There was no path.
        return -1

grid = [[0, 1], [1, 0]]
grid_2 = [[0, 1], [1, 0], [0, 0]]

solution = Solution()
print(solution.shortestPathBinaryMatrix(grid))
print(solution.shortestPathBinaryMatrix(grid_2))