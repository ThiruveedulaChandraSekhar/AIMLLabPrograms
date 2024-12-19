from itertools import permutations


def solve_crypto():
    # Define the letters involved in the equation
    letters = 'SENDMOREY'

    # Ensure unique digits for each letter using permutations
    # It generates every possible combination of 9 digits (from 0 to 9) to match our 9 letters.

    for perm in permutations(range(10), len(letters)):
        # Map letters to digits
        mapping = dict(zip(letters, perm))

        # The leading letters 'S' and 'M' cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Convert SEND, MORE, and MONEY to their respective integer values
        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']

        # Check if the equation holds
        if send + more == money:
            return mapping


# Solve the problem and display the result
solution = solve_crypto()
if solution:
    print("Solution found!")
    for letter, digit in solution.items():
        print(f"{letter} = {digit}")
else:
    print("No solution found.")
