# Hill Climbing for Mountain Peak Search

# 5x5 elevation grid
grid = [
    [10, 12, 14, 16, 18],
    [9, 11, 13, 17, 20],
    [8, 10, 15, 19, 22],
    [7, 9, 12, 21, 24],
    [5, 6, 8, 23, 25]
]

rows = len(grid)
cols = len(grid[0])

# Start from bottom-left corner
current = (rows - 1, 0)
path = [current]

# Possible moves: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    r, c = current
    current_value = grid[r][c]

    best = current
    best_value = current_value

    # Check all neighbors
    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] > best_value:
                best = (nr, nc)
                best_value = grid[nr][nc]

    # Stop if no better neighbor exists
    if best == current:
        break

    current = best
    path.append(current)

# Print path
print("Path followed:")
for p in path:
    print(f"{p} -> Elevation {grid[p[0]][p[1]]}")

print("\nHighest Reachable Peak:")
print("Position:", current)
print("Elevation:", grid[current[0]][current[1]])
