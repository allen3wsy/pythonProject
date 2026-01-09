from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_sum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        sums = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sums.append(sum)

        return sums
