

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

    def _search(self, root, key, parent_node=None, position="root"):
        if root:
            if root.value == key:
                return root, parent_node, position
            elif root.value < key:
                return self._search(root.right_child, key, root, "right")
            else:
                return self._search(root.left_child, key, root, "left")
        else:
            return -1, -1, None

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

    def get_delete_case(self, node_to_delete):
        if(not node_to_delete.left_child and not node_to_delete.right_child):
            print("\nNode to delete is LEAF node\n")
            return "CASE1"
        elif(node_to_delete.left_child and not node_to_delete.right_child):
            print("\nNode to delete has left child\n")
            return "CASE2"
        elif (not node_to_delete.left_child and node_to_delete.right_child):
            print("\nNode to delete has right child\n")
            return "CASE3"
        else:
            print("\nNode has both right and left child\n")
            return "CASE4"

    def _delete(self, delete_subtree_root, value, delete_parent_node=None):
        node_to_delete, parent_node, position = self._search(delete_subtree_root, value)
        if node_to_delete == -1:
            print("Node to delete not found in this tree")
            return delete_subtree_root
        else:
            case  = self.get_delete_case(node_to_delete)
            if not parent_node:
                parent_node = delete_parent_node
            if case == "CASE1":
                if position == "left":
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
                return delete_subtree_root
            elif case == "CASE2":
                parent_node.left_child = node_to_delete.left_child
                return delete_subtree_root
            elif case == "CASE3":
                parent_node.right_child = node_to_delete.right_child
                return delete_subtree_root
            else:
                actual_node_to_delete = self._min_value(node_to_delete.right_child)
                node_to_delete.value = actual_node_to_delete.value
                deleted_sub_tree = self._delete(node_to_delete.right_child, 
                    node_to_delete.value, node_to_delete)


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


bst.inorder()


deleted_tree = bst.delete(100)

bst.inorder()