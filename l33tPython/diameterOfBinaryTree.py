class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.width = 0
            
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.width = max(self.width, (left + right))
            
            return max(left, right) + 1
        
        dfs(root)
        
        return self.width