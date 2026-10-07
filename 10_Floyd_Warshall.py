n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
print("Enter 999 if there is no edge")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


for k in range(n):
    for i in range(n):
        for j in range(n):

            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


print("Shortest path matrix:")

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()
