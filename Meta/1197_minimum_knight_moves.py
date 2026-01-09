from collections import deque

class Solution:
    @staticmethod
    def minimum_knight_moves(x: int, y: int) -> int:
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # Step 1: Initialize the queue and visited set
        queue = deque([(0, 0, 0)])
        visited = set((0, 0))
        # Step 2: Perform BFS traversal
        while queue:
            # (cx, cy) is the current knight position
            cx, cy, moves = queue.popleft()

            if (cx, cy) == (x, y):
                return moves

            # check all possible moves of the knight from the current position
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                # if the new position is not visited yet, add it to the queue
                # also mark it as visited and increment the number of moves
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))

        # if the target position is not reachable, return -1
        return -1

print(Solution.minimum_knight_moves(1, 2))

print(Solution.minimum_knight_moves(1, 1))
print(Solution.minimum_knight_moves(2, 2))
print(Solution.minimum_knight_moves(3, 3))
print(Solution.minimum_knight_moves(4, 4))