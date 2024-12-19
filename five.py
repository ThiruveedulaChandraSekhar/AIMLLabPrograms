import random  # Import the random module to use random functions


# Function to check if a move is allowed
def is_valid_move(grid, x, y):
    # Check if the position (x, y) is within the grid and not blocked
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'obst'


# Function to calculate Manhattan distance between two points
def manhattan_distance(x1, y1, x2, y2):
    # Distance is the total steps in horizontal and vertical directions
    return abs(x1 - x2) + abs(y1 - y2)


# Function to perform the stochastic hill climbing algorithm
def stochastic_hill_climbing(grid, start, goal):
    x, y = start  # Start position
    x_goal, y_goal = goal  # Goal position

    while (x, y) != (x_goal, y_goal):  # Loop until we reach the goal
        # Possible moves (right, left, down, up)
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        # Only keep valid moves
        valid_moves = [move for move in neighbors if is_valid_move(grid, move[0], move[1])]

        if not valid_moves:  # If no valid moves, we're stuck
            print("Stuck at local optimum!")
            print("Failed to reach the goal.")
            return  # End the function

        # Pick a random valid move
        next_x, next_y = random.choice(valid_moves)

        # If the move brings us closer to the goal, take it
        if manhattan_distance(next_x, next_y, x_goal, y_goal) < manhattan_distance(x, y, x_goal, y_goal):
            x, y = next_x, next_y
            print(f"Current position: ({x}, {y})")
        else:
            print("Stuck at local optimum!")
            print("Failed to reach the goal.")
            return  # End the function

    print("Goal reached!")


# Example grid setup
grid = [
    ['free', 'free', 'free', 'obst'],
    ['free', 'obst', 'free', 'free'],
    ['free', 'free', 'free', 'obst'],
    ['free', 'free', 'free', 'free']
]

start = (0, 0)  # Start position
goal = (3, 3)  # Goal position

stochastic_hill_climbing(grid, start, goal)
