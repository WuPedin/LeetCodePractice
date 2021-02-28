class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
            graph = self.build_graph(seqs)
            order = self.topSort(graph)
            return order == org

    def build_graph(self, seqs):
        graph = {}
        # Add nodes
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        # Add edges
        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].add(seq[i + 1])

        return graph

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in graph[node]:
                node_to_indegree[neighbor] += 1

        return node_to_indegree

    def topSort(self, graph):
        
        # Check
        if not graph:
            return []

        # Get indegree of every nodes
        node_to_indegree = self.get_indegree(graph)

        # BFS
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            if len(queue) > 1:
                return None
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == len(graph):
            return order
        return None

        
