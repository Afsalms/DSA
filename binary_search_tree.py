

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
        



a = Node(13)
bst = BinarySearchTree()
bst.insert(a)
a = Node(3)
bst.insert(a)
a = Node(14)
bst.insert(a)
a = Node(1)
bst.insert(a)
a = Node(2)
bst.insert(a)
a = Node(4)
bst.insert(a)
a = Node(18)
bst.insert(a)


# print(bst)
print(bst.root)
print(bst.root.left_child)
print(bst.root.right_child)
print(bst.root.left_child.left_child)
print(bst.root.left_child.right_child)
print(bst.root.left_child.left_child.left_child)
print(bst.root.left_child.left_child.right_child)
print(bst.root.left_child.right_child)
print(bst.root.left_child.right_child.left_child)
print(bst.root.left_child.right_child.right_child)

print(bst.root.right_child.left_child)
print(bst.root.right_child.right_child)



