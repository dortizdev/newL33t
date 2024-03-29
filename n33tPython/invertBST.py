class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root