# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            point = root

            while point is not None:
                if p.val > point.val and q.val > point.val:
                    point = point.right
                elif p.val < point.val and q.val < point.val:
                    point = point.left
                else:
                    return point