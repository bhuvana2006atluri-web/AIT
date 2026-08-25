import random

d = [[0,10,15,20],
     [10,0,35,25],
     [15,35,0,30],
     [20,25,30,0]]

n = 4
pher = [[1]*n for _ in range(n)]
best, best_dist = None, float('inf')

for _ in range(100):
    for _ in range(10):
        route = [0]
        unvisited = set(range(1,n))

        while unvisited:
            cur = route[-1]
            nxt = min(unvisited,
                      key=lambda x: d[cur][x] / pher[cur][x])
            route.append(nxt)
            unvisited.remove(nxt)

        route.append(0)
        dist = sum(d[route[i]][route[i+1]]
                   for i in range(n))

        if dist < best_dist:
            best, best_dist = route, dist

print("Best Route:", best)
print("Shortest Distance:", best_dist)
