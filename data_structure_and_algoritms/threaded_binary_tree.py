import sys  
sys.setrecursionlimit(10000)  

class Node:

    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.is_right_threaded = False

    def __str__(self):
        return f"{self.value}"


class ThreadedBinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if type(node) != Node:
            node = Node(node)
        if not self.root:
            self.root = node
            self.root.right_child = node
            self.root.is_right_threaded = True
        self._insert(self.root, node)

    def _insert(self, root, node):
        if node.value > root.value:
            node.is_right_threaded = True
            if root.is_right_threaded == True:
                root.right_child = node
                node.is_right_threaded = True
                root.is_right_threaded = False
                if node.value < self.root.value:
                    node.right_child = self.root
            else:
                self._insert(root.right_child, node)
        elif node.value < root.value:
            if not root.left_child:
                root.left_child = node
                node.is_right_threaded = True
                node.right_child = root
            else:
                self._insert(root.left_child, node)

    def inorder(self):
        self._inorder(self.root)
        print("\n")

    def _inorder(self, root):
        if root:
            self._inorder(root.left_child)
            print(root, end=" ")
            self._inorder(root.right_child)

    def left_most_child(self, node=None):
        if not node:
            node = self.root
        left = node.left_child
        while node:
            left = node
            node = node.left_child
        return left

    def inorder_threaded(self):
        current_element = self.left_most_child()
        if not current_element:
            return 
        while current_element:
            import time
            print(current_element, end=" ")
            if current_element.is_right_threaded:
                current_element = current_element.right_child if current_element != self.root else None
            else:
                if current_element and current_element.right_child == self.root:
                    current_element = None
                else:
                    current_element = self.left_most_child(current_element.right_child)
        print("\n")

tbt = ThreadedBinaryTree()

#tbt.insert(100)
#tbt.insert(20)
#tbt.insert(10)
#tbt.insert(30)
#tbt.insert(200)
#tbt.insert(150)
#tbt.insert(149)
#tbt.insert(300)
#tbt.insert(301)
for i in range(2000):
    tbt.insert(i)

import time



start = time.time()
tbt.inorder_threaded()
end = time.time()
print("Time taken: ", end - start)


start = time.time()
tbt.inorder()
end = time.time()
print("Time taken: ", end - start)

