# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            columnTable[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))

        # [colTab[x] for x in range(min, max + 1) ]
        # with this we don't have to sort the index, which is N log(N)
        return [columnTable[x] for x in range(min_column, max_column + 1)]

# final time: O(N)
# final space: O(N)