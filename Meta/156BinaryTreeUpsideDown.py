# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        else:
            result = self.upsideDownBinaryTree(root.left)
            # Don't manipulate 'result' at every level since 'result' will only be the leftmost leave node !!!
            # This is wrong:: result.right = root 
            root.left.right = root
            
            # root.right can't be None
            root.left.left = root.right

            # unset root's 2 edges
            root.left = root.right = None
            return result
            

        
        