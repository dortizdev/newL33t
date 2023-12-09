class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diam[0] = max(diam[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return diam[0]