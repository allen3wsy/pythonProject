class Solution:

    # time log(N)
    # space log(N)
    def myPow(self, x: float, n: int) -> float:
        def binaryExp(x, n):
            if n == 0:
                return 1.0
            if n < 0:
                return 1.0 / (binaryExp(x, -n))

            if n % 2 == 1:
                return x * binaryExp(x * x, n // 2)
            else:
                return binaryExp(x * x, n // 2)

        return binaryExp(x, n)

solution = Solution()
print(solution.myPow(2, 3))
print(solution.myPow(2, -3))