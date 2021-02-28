DIRECTIONS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        
        # Check
        if not grid or not grid[0]:
            return -1

        # BFS
        n, m = len(grid), len(grid[0])
        queue = collections.deque([(0,0)])
        distance = {(0,0): 0}
        while queue:
            (x, y) = queue.popleft()
            for (dx, dy) in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(grid, next_x, next_y):
                    continue
                if (next_x, next_y) in distance:
                    continue 
                queue.append((next_x, next_y))
                distance[(next_x, next_y)] = distance[(x,y)] + 1
                if (next_x, next_y) == (n - 1, m - 1):
                    return distance[(next_x, next_y)]

        return -1

    def is_valid(self, grid, x, y):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        return not grid[x][y]
