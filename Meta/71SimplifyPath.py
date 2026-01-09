from collections import deque
#71. Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:

        # stack = []
        stack = deque()

        for portion in path.split("/"):
            if portion == "..":
                # Don't forget to check if the stack is empty, otherwise it will fail
                # to pop()
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                stack.append(portion)

        return '/' + '/'.join(stack)

# Create a new instance of the Solution class
solution = Solution()

print(solution.simplifyPath('a/b/c/k...'))
