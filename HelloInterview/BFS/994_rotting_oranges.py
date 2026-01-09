from collections import deque
# 0: Empty "E"
# 1: Fresh "F"
# 2: Orange "R"
# Also Meta
def rotting_oranges(grid: list[list[int]]) -> int:
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0
    # Step 1: Initialize BFS Queue and Count Fresh Oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # Step 2: Perform BFS to Simulate Rotting Process
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    minutes = 0
    while queue and fresh_oranges > 0:
        minutes += 1
        # process all the rotten oranges at the current minute
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:  # Fresh
                    grid[nx][ny] = 2  # "R"
                    fresh_oranges -= 1
                    queue.append((nx, ny))
    return minutes if fresh_oranges == 0 else -1


matrix = [[2, 1, 1],
          [1, 1, 0],
          [0, 1, 1]]
print(rotting_oranges(matrix))

