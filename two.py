# Write a Python program to implement a Random Movement Reflex Agent. (A, B and C).

import random
import time

# Define the locations
locations = ['A', 'B', 'C']

# Initial location of the agent
current_location = random.choice(locations)


# Function to simulate the agent's random movement
def move_agent(current_location):
    # Choose a random next location
    next_location = random.choice(locations)
    print(f"Agent moved from {current_location} to {next_location}")
    return next_location


# Simulate the agent's random movement for a specified number of steps
def simulate_random_movement(steps):
    global current_location

    for _ in range(steps):
        current_location = move_agent(current_location)
        time.sleep(1)  # Wait for a second before the next move


# Number of steps the agent will take
steps = 10

# Start the simulation
print(f"Starting location: {current_location}")

simulate_random_movement(steps)

print(f"Final location: {current_location}")