def dfs(root):
    if root is not None:
        dfs(root.left)
        dfs(root.right)
        return root