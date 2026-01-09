class Solution:
    def minInsertions(self, s):
        # result: the number of left/right parentheses already added.
        # rToAdd: the number of right parentheses needed.
        result = rToAdd = 0
        for c in s:
            if c == '(':
                # EX: ()( )( ))), for this case the answer should be 4
                # "()("
                if rToAdd % 2 == 1:
                    rToAdd -= 1
                    result += 1
                rToAdd += 2
            if c == ')':
                rToAdd -= 1
                if rToAdd < 0:
                    rToAdd += 2
                    result += 1
        return rToAdd + result


# test case 1: (
# test case 2: ()
# test case 3: )
# test case 4: ))
# test case 5: )(
# test case 6: ()() ()))

solution = Solution()
print(solution.minInsertions("()()()))"))
print(solution.minInsertions("()("))
# print(solution.canConstruct("leetcode", 5))
