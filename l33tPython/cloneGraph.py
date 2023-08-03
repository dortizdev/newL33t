class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeClones = {}

        def dfs(node):
            if node in nodeClones:
                return nodeClones[node]

            clonedGraph = Node(node.val)
            nodeClones[node] = clonedGraph
            
            for i in node.neighbors:
                clonedGraph.neighbors.append(dfs(i))
            return clonedGraph

        return dfs(node) if node else None