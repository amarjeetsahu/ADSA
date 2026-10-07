from collections import deque

n = int(input("Enter number of vertices: "))

graph = [[] for i in range(n)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)


start = int(input("Enter starting vertex: "))

visited = [False] * n
queue = deque()

queue.append(start)
visited[start] = True

print("BFS traversal:")

while queue:
    vertex = queue.popleft()

    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)
