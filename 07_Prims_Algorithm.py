n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


selected = [False] * n
selected[0] = True

print("Edges in MST:")

total = 0

for i in range(n - 1):

    minimum = 999
    x = 0
    y = 0

    for j in range(n):
        if selected[j]:

            for k in range(n):
                if not selected[k] and graph[j][k] < minimum:
                    minimum = graph[j][k]
                    x = j
                    y = k

    print(x, "-", y, ":", minimum)

    total += minimum
    selected[y] = True

print("Minimum cost:", total)
