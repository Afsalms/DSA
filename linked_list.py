
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if not self.head:
            return "[]"
        current_node = self.head
        text = ''
        while current_node:
            text += str(current_node.value) + "->"
            current_node = current_node.next
        return text[:-2]

    def add_item(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if not self.head:
            self.head = item
       	    self.tail = item
            self.head.next = item
        self.tail.next = item
        self.tail = item

    def search_item(self, value):
        is_found = False
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == value:
                is_found = True
                break
            current_node = current_node.next
            index += 1
        if is_found:
            return index, current_node
        else:
            return -1, None

a = Node(1)
b = Node(2)
c = Node(3)

ll = LinkedList()
#print(ll)

ll.add_item(a)
ll.add_item(b)
ll.add_item(c)
ll.add_item(10)
ll.add_item(50)

#print(ll)


index, current_node = ll.search_item(10)
print(index, current_node, current_node.next, current_node.next.next)
index, current_node = ll.search_item(100)
print(index, current_node)
