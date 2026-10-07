class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    root = insert(root, data)

print("Inorder traversal:")
inorder(root)

key = int(input("\nEnter key to search: "))

if search(root, key):
    print("Key found")
else:
    print("Key not found")
