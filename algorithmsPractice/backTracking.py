def visit_all_points(curr_pos, curr_path, visited, total_points, dest_point):
    # Base case: if the current position is equal to the destination point B and the set of visited points contains all points on the grid (excluding any "x" points), increment the count variable by 1 and return it.
    if curr_pos == dest_point and len(visited) == total_points:
        return 1
    
    count = 0
    # Check all neighboring points of the current position
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Compute the coordinates of the neighboring point
        next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
        # Check if the neighboring point is within the grid boundaries and hasn't been visited yet and is not an "x" point
        if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and next_pos not in visited and grid[next_pos[0]][next_pos[1]] != "x":
            # Mark the neighboring point as visited in the set of visited points
            visited.add(next_pos)
            # Add the neighboring point to the current path
            curr_path.append(next_pos)
            # Recursively call the "visit_all_points" function with the neighboring point as the current position, the updated current path, the updated set of visited points, the total number of points on the grid, and the final destination point B. Add the returned count to the current count.
            count += visit_all_points(next_pos, curr_path, visited, total_points, dest_point)
            # Remove the neighboring point from the current path and the set of visited points
            curr_path.pop()
            visited.remove(next_pos)
    
    return count


# Example usage
grid = [
    ["A", ".", ".", "."],
    [".", ".", "x", "."],
    [".", ".", ".", "."],
    [".", "x", ".", "B"]
]

# Count the total number of points on the grid (excluding any "x" points)
total_points = sum(1 for row in grid for cell in row if cell != "x")
# Define the starting point and the destination point
start_point = (0, 0)
dest_point = (len(grid) - 1, len(grid[0]) - 1)
# Mark the starting point as visited and add it to the current path
visited = {start_point}
curr_path = [start_point]
# Call the "visit_all_points" function with the starting point as the current position, the current path, the set of visited points, the total number of points on the grid, and the final destination point B.
count = visit_all_points(start_point, curr_path, visited, total_points, dest_point)

# Print the count of ways the robot can move from A to B and visit all points along the way
print(count)  # Output: 2
