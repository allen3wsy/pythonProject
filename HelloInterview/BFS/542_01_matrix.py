from collections import deque


# Also Meta tag
# BFS from existing "0" positions
class Solution:
    @staticmethod
    def update_matrix(mat):
        rows, cols = len(mat), len(mat[0])

        # init 2D matrix with all -1...
        output = [[-1] * cols for _ in range(rows)]
        queue = deque()
        # Step 1: Initialize the queue with all the 0 cells
        # set their distance to 0 in the output grid
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    output[r][c] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Step 2: Perform BFS traversal
        distance = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if output[nr][nc] == -1:
                            output[nr][nc] = distance
                            queue.append((nr, nc))
            distance += 1
        # Step 5: Return the output grid
        return output


mat = [[0, 0, 0],
       [0, 1, 0],
       [1, 1, 1]]

print(Solution.update_matrix(mat))
