import heapq

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'E': 1},
    'D': {'F': 2},
    'E': {'F': 3, 'G': 4},
    'F': {'G': 2},
    'G': {}
}

# Heuristic: estimated distance to G
h = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 'F': 2, 'G': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        for nxt, distance in graph[node].items():
            new_cost = cost + distance
            heapq.heappush(
                pq, (new_cost + h[nxt], new_cost, nxt, path + [nxt])
            )

path, cost = astar('A', 'G')

print("Shortest Route:", " -> ".join(path))
print("Total Distance:", cost)
