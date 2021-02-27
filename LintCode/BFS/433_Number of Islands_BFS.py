class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        
        # Check
        if not grid or not grid[0]:
            return 0
        
        # Initialize
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        num_islands = 0

        # BFS
        for i in range(n):
            for j in range(m):
                
                if visited[i][j]:
                    continue 
                visited[i][j] = True
                if grid[i][j] == 0:
                    continue 

                # If grid[i][j] is an island, search adjancency area if there is any island
                self.find_islands(i, j, grid, visited, n, m)
                num_islands += 1

        return num_islands

    def find_islands(self, i, j, grid, visited, n, m):
        queue = collections.deque([[i,j]])
        while queue:
            q = queue.popleft()
            i, j = q[0], q[1]

            # If is island, append adjancency area
            if i < n - 1 and not visited[i + 1][j]:
                if grid[i + 1][j] == 1:
                    queue.append([i + 1, j])  
                visited[i + 1][j] = True
            if j < m - 1 and not visited[i][j + 1]:
                if grid[i][j + 1] == 1:
                    queue.append([i, j + 1])
                visited[i][j + 1] = True
            if i > 0 and not visited[i - 1][j]:
                if grid[i - 1][j] == 1:
                    queue.append([i - 1, j])  
                visited[i - 1][j] = True
            if j > 0 and not visited[i][j - 1]:
                if grid[i][j - 1] == 1:
                    queue.append([i, j - 1])
                visited[i][j - 1] = True

