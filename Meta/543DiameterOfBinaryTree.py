# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Define outside longest_path() function!
        diameter = 0

        def longest_path(node):
            if not node:
                return 0
            
            # Critical !!!
            nonlocal diameter

            # recursively find the longest path in
            # both left child and right
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        # Don't care about the return of this line since it only returns the longest
        # one-sided path upwards.
        longest_path(root)

        # Only care about this result!
        return diameter
