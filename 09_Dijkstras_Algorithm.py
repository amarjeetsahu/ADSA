n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex: "))

distance = [999] * n
visited = [False] * n

distance[source] = 0


for i in range(n):

    minimum = 999
    u = -1

    for j in range(n):
        if not visited[j] and distance[j] < minimum:
            minimum = distance[j]
            u = j

    if u == -1:
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance


print("Shortest distances:")

for i in range(n):
    print(source, "to", i, "=", distance[i])
