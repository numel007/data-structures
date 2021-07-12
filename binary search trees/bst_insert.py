class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_nonroot(self, val, current=None):
        if current == None:
            current = Node(val)
        elif current.info > val:
            current.left = self.insert_nonroot(val, current.left)
        else:
            current.right = self.insert_nonroot(val, current.right)

        return current

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.insert_nonroot(val, self.root)


tree = BinarySearchTree()
arr = [4, 2, 3, 1, 7, 6]

for i in range(len(arr)):
    print(f'Inserting {arr[i]}')
    tree.insert(arr[i])

preOrder(tree.root)
