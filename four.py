import heapq


# Define the PuzzleState class
class PuzzleState:
    def __init__(self, board, empty_pos, moves=0, previous=None):
        self.board = board  # Current board configuration
        self.empty_pos = empty_pos  # Position of the empty tile (0)
        self.moves = moves  # Number of moves taken to reach this state
        self.previous = previous  # Reference to the previous state for path reconstruction
        self.cost = self.moves + self.heuristic()  # Total cost (moves + heuristic)

    def heuristic(self):
        # Calculate the number of misplaced tiles heuristic
        misplaced = 0
        goal = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]]
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != 0 and self.board[i][j] != goal[i][j]:
                    misplaced += 1  # Count the number of misplaced tiles
        return misplaced

    def get_neighbors(self):
        neighbors = []  # List to store neighboring states
        x, y = self.empty_pos  # Current position of the empty tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves (up, down, left, right)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # New position of the empty tile
            if 0 <= nx < 4 and 0 <= ny < 4:  # Check if the new position is within bounds
                new_board = [row[:] for row in self.board]  # Create a copy of the current board
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]  # Swap tiles
                neighbors.append(PuzzleState(new_board, (nx, ny), self.moves + 1, self))  # Create new state
        return neighbors

    def __lt__(self, other):
        return self.cost < other.cost  # Comparison operator for priority queue

    def __eq__(self, other):
        return self.board == other.board  # Equality check based on board configuration

    def __hash__(self):
        return hash(
            tuple(tuple(row) for row in self.board))  # Hash function for storing states in sets and dictionaries


# A* search algorithm
def a_star_search(initial_board):
    # Find the initial position of the empty tile
    initial_pos = [(i, row.index(0)) for i, row in enumerate(initial_board) if 0 in row][0]
    initial_state = PuzzleState(initial_board, initial_pos)  # Create the initial state

    open_set = []  # Priority queue (min-heap) for the open set
    heapq.heappush(open_set, initial_state)  # Add the initial state to the open set
    closed_set = set()  # Set to keep track of visited states

    while open_set:  # Main loop of the A* algorithm
        current_state = heapq.heappop(open_set)  # Get the state with the lowest cost

        if current_state.heuristic() == 0:  # Check if the goal state is reached
            return reconstruct_path(current_state)  # Reconstruct and return the solution path

        closed_set.add(current_state)  # Add the current state to the closed set

        for neighbor in current_state.get_neighbors():  # Generate neighboring states
            if neighbor not in closed_set:  # If the neighbor has not been visited
                heapq.heappush(open_set, neighbor)  # Add it to the open set

    return None  # Return None if no solution is found


# Function to reconstruct the solution path from the goal state to the initial state
def reconstruct_path(state):
    path = []  # List to store the solution path
    while state:  # Trace back from the goal state to the initial state
        path.append(state.board)  # Add the current board to the path
        state = state.previous  # Move to the previous state
    path.reverse()  # Reverse the path to get the correct order from initial to goal
    return path


# Example usage
initial_board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 0, 15]
]
print("Initial State:")
for row in initial_board:
    print(row)
print()

solution = a_star_search(initial_board)  # Find the solution using A* search

if solution:
    print("Solution found!")
    print("Goal State:")
    for row in solution[-1]:
        print(row)
    print()

    print("Steps to reach the goal state:")
    for step in solution:  # Print the solution path step by step
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
