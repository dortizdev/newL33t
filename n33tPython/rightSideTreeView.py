class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        queue = collections.deque([root])

        while queue:
            rightNode = None
            queueLen = len(queue)

            for i in range(queueLen):
                n = queue.popleft()
                if n:
                    rightNode = n
                    queue.append(n.left)
                    queue.append(n.right)

            if rightNode:
                answer.append(rightNode.val)
        return answer