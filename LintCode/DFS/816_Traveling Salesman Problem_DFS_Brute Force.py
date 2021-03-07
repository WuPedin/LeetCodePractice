# 做DFS要小心答案的存儲，不要存到同個記憶體位置，答案會一樣
class Result:
    def __init__(self):
        self.min_cost = float('inf')

class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.construct_graph(n, roads)
        result = Result()
        self.dfs(1, n, set([1]), 0, graph, result)
        return result.min_cost

    def dfs(self, city, n, visited, cost, graph, result):
        # 出口
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return 
        
        # 拆解
        for next_city in graph[city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)


    # graph records all min costs from city A to city B
    def construct_graph(self, n, roads):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)} 
            for i in range(1, n + 1)
        }
        # There are multiple roads to travel between city A and B
        for A, B, c in roads:
            graph[A][B] = min(graph[A][B], c)
            graph[B][A] = min(graph[B][A], c)
        return graph
