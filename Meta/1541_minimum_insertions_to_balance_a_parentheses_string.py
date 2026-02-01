
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
# any '(' needs two consecutive ')' to be balanced and the 2 ')' need to be before next '('
# e.g. "())", "())(())))" and "(())())))" are balanced
class Solution:
    def min_insertions(self, s):
        # alreadyAdded: the number of insertions needed.
        # rToAdd: the number of right parentheses needed.
        alreadyAdded = rToAdd = 0
        for c in s:
            if c == '(':
                # EX: ()( )( ))), for this case the answer should be 4
                # "()("
                if rToAdd % 2 == 1:
                    rToAdd -= 1
                    alreadyAdded += 1 # adding a ')' before the current '(' hence alreadyAdded += 1
                rToAdd += 2
            if c == ')':
                rToAdd -= 1
                if rToAdd < 0: # adding a '(', hence alreadyAdded += 1
                    rToAdd += 2
                    alreadyAdded += 1 
        return rToAdd + alreadyAdded


# test case 1: (
# test case 2: ()
# test case 3: )
# test case 4: ))
# test case 5: )(
# test case 6: ()() ()))

solution = Solution()
print(solution.min_insertions("()()()))")) # 4

# have to study this test case:
# when there is only one ')' and we encounter '(', we need to add one more ')'.

print(solution.min_insertions("()(")) # 3
