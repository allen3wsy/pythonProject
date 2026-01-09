from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer
            if node:
                # low <= node.val and node.val <= high
                if low <= node.val <= high:
                    answer += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        dfs(root)
        return answer

# O(N): time
# O(N): space
