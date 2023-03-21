class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeVals = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            level = []
            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                nodeVals.append(level)

        return nodeVals