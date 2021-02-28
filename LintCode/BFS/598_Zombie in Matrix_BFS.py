DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        
        # Check 
        if not grid or not grid[0]:
            return -1

        # Get all zombies
        zombies, num_walls = self.chk_status(grid)
        queue = collections.deque(list(zombies.keys()))
        days = 0

        while queue:
            # Zombie
            (x, y) = queue.popleft()

            # Start infect human by BFS
            for (dx, dy) in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if self.is_valid(next_x, next_y, grid, zombies):
                    zombies[(next_x, next_y)] = zombies[(x,y)] + 1
                    queue.append((next_x, next_y))
                    days = max(days, zombies[(x,y)] + 1)

        if len(zombies) + num_walls == len(grid) * len(grid[0]):
            return days
        return -1
        

    def is_valid(self, x, y, grid, zombies):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if grid[x][y] == 2:
            return False
        return (x, y) not in zombies

    
    def chk_status(self, grid):
        zombies = {}
        num_walls = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    zombies[(i,j)] = 0
                elif grid[i][j] == 2:
                    num_walls += 1
        return zombies, num_walls



    


    
