class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root