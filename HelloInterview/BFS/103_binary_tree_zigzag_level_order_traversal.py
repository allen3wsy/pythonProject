from collections import deque

class Solution:
    @staticmethod
    def zig_zag(root):
        if not root:
            return []
        nodes = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            nodes_for_level = deque()
            # process all nodes at this level
            for i in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    # add the node to the back of the list
                    nodes_for_level.append(node.val)
                else:
                    # add the node to the front of the list
                    nodes_for_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # we've processed all nodes at the current level
            # add them to the output list and toggle left_to_right
            # to prepare for the next level
            nodes.append(list(nodes_for_level))
            left_to_right = not left_to_right
        return nodes
