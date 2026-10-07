class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    data = int(input("Enter data (-1 for no node): "))

    if data == -1:
        return None

    root = Node(data)

    print("Enter left child of", data)
    root.left = create_tree()

    print("Enter right child of", data)
    root.right = create_tree()

    return root


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = create_tree()

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)
