 # Buildings: A, B, C, D
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = {}

def can_color(vertex, color):
    return all(colors.get(neighbor) != color for neighbor in graph[vertex])

for vertex in graph:
    for color in range(1, 4):
        if can_color(vertex, color):
            colors[vertex] = color
            break

print("Coloring:", colors)
print("Map can be colored using 3 colors.")
