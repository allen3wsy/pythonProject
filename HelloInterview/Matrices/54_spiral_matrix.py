
# Meta
def spiral_order(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix:
        # [a,b] + [c] = [a,b,c]. list only has pop(0). dequeue has popleft()
        # top row
        result += matrix.pop(0)
        # right column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        # bottom row
        if matrix:
            result += matrix.pop()[::-1]
        # left column (down to up)
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


matrix = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

print(matrix)
print(spiral_order(matrix))