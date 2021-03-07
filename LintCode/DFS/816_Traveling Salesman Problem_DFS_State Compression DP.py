class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.construct_graph(n, roads)
        # state_size應該是2的n次方-1
        # 1 << 2 -> 100 = 4, 所以1 << n = 2的n次方
        state_size = 1 << n 
        # f[21][3]代表我經過了21的狀態，最後停在3的點
        f = [
            [float('inf')] * (n + 1)
            for _ in range(state_size)
        ]
        f[1][1] = 0
        for state in range(state_size):
            for i in range(2, n + 1):
                if state & (1 << (i - 1)) == 0:
                    continue 
                # XOR比減法快，XOR也可以做減法
                # prev_state = state - 2的i-1次方
                # 1<<x，1左移x位，1<<2=100=4，所以它是2的i-1次方
                prev_state = state ^ (1 << (i - 1))
                for j in range(1, n + 1):
                    # 如果visited，=2的(j-1)次方
                    if prev_state & (1 << (j - 1)) == 0:
                        continue
                    # 動態規劃的公式，固定頭尾，f[state][i] = f[prev_state][j] + graph[j][i]
                    # 打擂臺，要找一個j使得f[state][i]最短
                    f[state][i] = min(f[state][i], f[prev_state][j] + graph[j][i])
        # 2的n次方-1相當於n個1，111111...就是我們最後要的，然後取最小值即可
        return min(f[state_size - 1])
    

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
