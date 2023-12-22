class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(sL,sR):
            if not sL and not sR:
                return True
            if not sL or not sR:
                return False

            return (sL.val == sR.val and 
            dfs(sL.left, sR.right) and 
            dfs(sL.right, sR.left))
        return dfs(root.left, root.right)