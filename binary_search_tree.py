

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

    def level_order(self):
        self._level_order(self.root)
        print("\n")

    def _level_order(self, root_node):
        nodes_to_process = []
        nodes_to_process.append(root_node)
        while nodes_to_process:
            current_node = nodes_to_process.pop(0)
            print(current_node, end=" ")
            if current_node.left_child:
                nodes_to_process.append(current_node.left_child)
            if current_node.right_child:
                nodes_to_process.append(current_node.right_child)



bst = BinarySearchTree()
bst.insert(100)
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(200)
bst.insert(150)
bst.insert(300)


bst.preorder()
bst.inorder()
bst.postorder()
bst.level_order()



