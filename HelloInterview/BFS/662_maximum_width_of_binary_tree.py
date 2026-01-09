from HelloInterview.BFS.level_order_sum import TreeNode
from collections import deque


class Solution:
    @staticmethod
    def max_width(root: TreeNode) -> int:
        if not root:
            return 0
        # enqueue the root node with position 0
        queue = deque([(root, 0)])
        max_ = 0
        while queue:
            level_size = len(queue)
            # left_pos is the position of the leftmost node at the current level
            _, left_pos = queue[0]
            right_pos = -1
            for i in range(level_size):
                node, pos = queue.popleft()
                # update right_pos to the position of the rightmost node
                # when we reach the last node in the level
                if i == level_size - 1:
                    right_pos = pos
                # add the children to the queue with their positions
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))

            # right_pos - left_pos + 1 is the width of the current level
            max_ = max(max_, right_pos - left_pos + 1)
        return max_
