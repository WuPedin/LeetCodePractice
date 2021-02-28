"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        visited = set()
        res = []

        for node in nodes:
            if node in visited:
                continue 
            visited.add(node)
            queue = collections.deque([node])
            res_tmp = []
            while queue:
                n = queue.popleft()
                res_tmp.append(n.label)
                for neighbor in n.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            res.append(sorted(res_tmp))
        
        return res

