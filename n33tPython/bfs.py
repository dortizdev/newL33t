def bfs(root):
    q = []
    q.append(root)

    while q:
        for i in range(len(q)):
            node = q.pop(0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)