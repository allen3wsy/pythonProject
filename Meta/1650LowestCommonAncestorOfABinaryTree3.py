# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q

        # pick an example: edge_1 = 3 and edge_2 = 5 and common anceter to root: 2
        while p1 != p2:
            if p1.parent:
                p1 = p1.parent
            else:  # "p1 = p" is also fine, but this is faster
                p1 = q
            if p2.parent:
                p2 = p2.parent
            else:  # "p1 = q" is also fine, but this is faster
                p2 = p
        return p1
