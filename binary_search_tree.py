

class Node:
    
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value


    def __str__(self):
        return f"{self.value}"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if type(node) != Node:
            node = Node(node)
        if not self.root:
            self.root = node
        self._insert(self.root, node)

    def _insert(self, root, node):
        if node.value > root.value:
            if not root.right_child:
                root.right_child = node
            else:
                self._insert(root.right_child, node)
        elif node.value < root.value:
            if not root.left_child:
                root.left_child = node
            else:
                self._insert(root.left_child, node)

    def preorder(self):
        self._preorder(self.root)
        print("\n")

    def _preorder(self, root):
        if root:
            print(root, end=' ')
            self._preorder(root.left_child)
            self._preorder(root.right_child)

    def inorder(self):
        self._inorder(self.root)
        print("\n")

    def _inorder(self, root):
        if root:
            self._inorder(root.left_child)
            print(root, end=" ")
            self._inorder(root.right_child)


    def postorder(self):
        self._postorder(self.root)
        print("\n")

    def _postorder(self, root):
        if root:
            self._postorder(root.left_child)
            self._postorder(root.right_child)
            print(root, end=" ")

    def search(self, key):
        self._search(self.root, key)

    def _search(self, root, key):
        if root:
            if root.value == key:
                print("value found")
            elif root.value < key:
                self._search(root.right_child, key)
            else:
                self._search(root.left_child, key)
        else:
            print("Value not found")
        



bst = BinarySearchTree()
a = Node("F")
bst.insert(a)

a = Node("D")
bst.insert(a)

a = Node("J")
bst.insert(a)

bst.insert("B")

a = Node("E")
bst.insert(a)


bst.insert("G")

bst.insert("K")

a = Node("I")
bst.insert(a)

a = Node("A")
bst.insert(a)

a = Node("B")
bst.insert(a)

bst.insert("C")

bst.preorder()
bst.inorder()
bst.postorder()



bst.search("A")

bst.search("J")

bst.search("Q")
bst.search("Z")




