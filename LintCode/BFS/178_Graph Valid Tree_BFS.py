class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        """
        To be a tree:
            1. Number of edges should be n - 1
            2. Nodes should be connected
        """

        # Check
        if len(edges) != n - 1:
            return False 

        # Find neighbors
        neighbors = {i:[] for i in range(n)}
        for i, j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        # Connect nodes by BFS
        visited = set()
        queue = collections.deque([0])
        visited.add(0)

        while queue:
            node = queue.popleft()
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == n


