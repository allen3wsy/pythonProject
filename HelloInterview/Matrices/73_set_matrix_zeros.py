# Meta tag
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for row in zero_rows:
        for col in range(cols):
            matrix[row][col] = 0
    for col in zero_cols:
        for row in range(rows):
            matrix[row][col] = 0
    return matrix


matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]

print(matrix)
print(set_zeroes(matrix))