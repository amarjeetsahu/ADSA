size = 10
table = [-1] * size


def hash_function(key):
    return key % size


def insert(key):
    index = hash_function(key)

    while table[index] != -1:
        index = (index + 1) % size

    table[index] = key


n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

print("Hash table:")

for i in range(size):
    print(i, ":", table[i])
