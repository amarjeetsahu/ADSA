n = int(input("Enter number of programs: "))

programs = []

for i in range(n):
    length = int(input("Enter program length: "))
    programs.append(length)

programs.sort()

print("Optimal storage order:")

for length in programs:
    print(length, end=" ")

total_time = 0
current_time = 0

for length in programs:
    current_time += length
    total_time += current_time

mrt = total_time / n

print("\nMean Retrieval Time:", mrt)
