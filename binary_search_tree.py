class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

# --- Main Program ---
if _name_ == "_main_":
    tree = BST()
    root = None

    # Insert nodes
    for val in [50, 30, 70, 20, 40, 60, 80]:
        root = tree.insert(root, val)

    print("Inorder Traversal:")
    tree.inorder(root)

    print("\nPreorder Traversal:")
    tree.preorder(root)

    print("\nPostorder Traversal:")
    tree.postorder(root)

    # Search example
    key = 40
    if tree.search(root, key):
        print(f"\nNode {key} found in BST.")
    else:
        print(f"\nNode {key} not found.")
