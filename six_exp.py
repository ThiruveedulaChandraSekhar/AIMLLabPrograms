from collections import deque

def min_steps_to_destination(grid, k):
    # Directions for moving up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m, n = len(grid), len(grid[0])

    # Queue will store (x, y, steps, obstacles_removed)
    queue = deque([(0, 0, 0, 0)])

    # Visited set to store (x, y, obstacles_removed)
    visited = set()
    visited.add((0, 0, 0))

    while queue:
        x, y, steps, obstacles_removed = queue.popleft()

        # If we reach the bottom-right corner
        if x == m - 1 and y == n - 1:
            return steps

        # Explore the neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the next cell is within bounds
            if 0 <= nx < m and 0 <= ny < n:
                new_obstacles_removed = obstacles_removed + grid[nx][ny]

                # If we haven't removed more obstacles than allowed and haven't visited this state
                if new_obstacles_removed <= k and (nx, ny, new_obstacles_removed) not in visited:
                    visited.add((nx, ny, new_obstacles_removed))
                    queue.append((nx, ny, steps + 1, new_obstacles_removed))

    # If we exhaust the queue without finding a path
    return -1

# Test the function with the provided input
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
print(f"The min. no. of steps to walk from the upper left corner to the lower right corner is = ", min_steps_to_destination(grid, k))