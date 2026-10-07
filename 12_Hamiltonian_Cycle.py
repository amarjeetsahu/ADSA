n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


path = [-1] * n
path[0] = 0


def is_safe(vertex, position):

    if graph[path[position - 1]][vertex] == 0:
        return False

    if vertex in path:
        return False

    return True


def hamiltonian(position):

    if position == n:

        if graph[path[position - 1]][path[0]] == 1:
            return True

        return False

    for vertex in range(1, n):

        if is_safe(vertex, position):

            path[position] = vertex

            if hamiltonian(position + 1):
                return True

            path[position] = -1

    return False


if hamiltonian(1):

    print("Hamiltonian Cycle:")

    for vertex in path:
        print(vertex, end=" ")

    print(path[0])

else:
    print("No Hamiltonian Cycle exists")
