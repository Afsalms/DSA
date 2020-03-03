

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
        return self._search(self.root, key)

    def _search(self, root, key, parent_node=None):
        if root:
            if root.value == key:
                return root, parent_node
            elif root.value < key:
                return self._search(root.right_child, key, root)
            else:
                return self._search(root.left_child, key, root)
        else:
            return -1, -1

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

    def min_value(self):
        return self._min_value(self.root)

    def _min_value(self, root_node):
        current_node = root_node
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node

    def delete(self, value):
        return self._delete(self.root, value)

    def _delete(self, root, value):
        import time
        time.sleep(0.01)
        node_to_delete, parent_node = self.search(value)
        print(node_to_delete, parent_node)
        print("++++++++++++++")
        if node_to_delete == -1:
            print("Node to delete not found in this tree")
        else:
            print("Node to delete is :", node_to_delete)
            if (not node_to_delete.left_child and not node_to_delete.right_child):
                if not parent_node:
                    self.root = None
                    del(node_to_delete)
                else:
                    if parent_node.left_child == node_to_delete:
                        parent_node.left_child = None
                    else:
                        parent_node.right_child = None
                    del(node_to_delete)
            elif (not node_to_delete.left_child and node_to_delete.right_child):
                parent_node.right_child = node_to_delete.right_child
                del(node_to_delete)
            elif (node_to_delete.left_child and not node_to_delete.right_child):
                parent_node.left_child = node_to_delete.left_child
                del(node_to_delete)
            else:
                print("case4 has both left and right subtree")
                min_node_right_tree = bst._min_value(node_to_delete.right_child)
                print(min_node_right_tree)
                print("++++++++++++++++++++++++")
                #node_to_delete.value = min_node_right_tree.value
                #self._delete(min_node_right_tree, min_node_right_tree.value)


bst = BinarySearchTree()
bst.insert(100)
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(200)
bst.insert(150)
bst.insert(149)
bst.insert(300)
bst.insert(301)


bst.preorder()
bst.inorder()
bst.postorder()
bst.level_order()


min_node = bst.min_value()

print("min_node: ", min_node)


#bst.delete(30)
#bst.preorder()
#bst.inorder()
#a, b = bst.search(200)
#print(a.right_child)
#print(a.left_child)
#print("+++++++++++++++")

bst.delete(20)

#bst.delete(150)
#bst.delete(300)

bst.preorder()
bst.inorder()


#a, b  = bst.search(200)
#print(a.right_child)
#print(a.left_child)
#print("++++++++++++++++++++++++++++++++++++++++")
