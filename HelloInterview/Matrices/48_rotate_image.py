# Meta
class Solution:

    @staticmethod
    def rotate_image(matrix: list[list[int]]):

        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = \
                    matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            # matrix[i] = matrix[i][::-1]   # this also works
            matrix[i].reverse()

matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print(matrix)
Solution.rotate_image(matrix)
print(matrix)