"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), 
              (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        
        # Check 
        if not grid or not grid[0]:
            return -1

        # Initialize
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue 
                if not self.is_valid(grid, next_x, next_y):
                    continue 
                queue.append((next_x, next_y))
                distance[(next_x, next_y)] = distance[(x, y)] + 1

        return -1


    def is_valid(self, grid, x, y):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False 
        return not grid[x][y]
