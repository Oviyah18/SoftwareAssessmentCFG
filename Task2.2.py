def count_squares_pattern(x):
    if x <= 0:
        return 0
    else:
        current_row_squares = x**2
        #recursion
        remaining_squares = count_squares_pattern(x-1)
        return current_row_squares + remaining_squares

# User input
grid_size = int(input("Enter the grid size: "))
num_squares = count_squares_pattern(grid_size)
print(f"A {grid_size}x{grid_size} grid has {num_squares} squares.")
