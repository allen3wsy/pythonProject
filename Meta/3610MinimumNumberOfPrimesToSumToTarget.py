import math

class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        # for i in range(2, int(num ** 0.5) + 1):
        for i in range(2, math.ceil(num ** 0.5)):

            if num % i == 0:
                return False
        return True

    def get_first_m_primes(self, m):
        primes = []
        num = 2
        while len(primes) < m:
            if self.is_prime(num):
                primes.append(num)
            num += 1
        return primes

    def minNumberOfPrimes(self, n: int, m: int) -> int:
        primes = self.get_first_m_primes(m)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for prime in primes:
            for i in range(prime, n + 1):
                if dp[i - prime] + 1 < dp[i]:
                    dp[i] = dp[i - prime] + 1

        if dp[n] != float('inf'):
            return dp[n]
        else:
            return -1
        # return dp[n] if dp[n] != float('inf') else -1

solution = Solution()
print(solution.minNumberOfPrimes(10, 2))
print(solution.minNumberOfPrimes(7, 6))

# Example 1:
# Input: n = 10, m = 2
# Output: 4
# Explanation:
# The first 2 primes are [2, 3]. The sum 10 can be formed as 2 + 2 + 3 + 3, requiring 4 primes.
#
# Example 3:
# Input: n = 7, m = 6
# Output: 1
# Explanation:
# The first 6 primes are [2, 3, 5, 7, 11, 13]. The sum 7 can be formed directly by prime 7, requiring only 1 prime.