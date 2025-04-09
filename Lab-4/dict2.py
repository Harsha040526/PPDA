# Create a dictionary with numbers and their squares
squares = {x: x*x for x in range(6)}
print(squares) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Dictionary with squares of odd numbers
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares) # Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
