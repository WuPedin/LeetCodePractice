from collections import deque

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Check 
        if not grid or not grid[0]:
            return 0
        
        # Initialize
        num_islands = 0
        visited = set()
        
        # BFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.bfs(i, j, grid, visited)
                    num_islands += 1
                    
        return num_islands
    
    def bfs(self, i, j, grid, visited):
        queue = deque([(i,j)])
        visited.add((i,j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(next_x, next_y, grid, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                
    def is_valid(self, x, y, grid, visited):
        m, n = len(grid), len(grid[0])
        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x,y) in visited:
            return False
        if grid[x][y] == "0":
            return False
        return True
                
            
        
                    