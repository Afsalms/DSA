
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if not self.head:
            return "[]"
        current_node = self.head
        text = str(self.head) + "->"
        while current_node.next and current_node.next != self.head:
            current_node = current_node.next
            text += str(current_node.value) + "->"
        text = text[:-2] + "-^"
        return text

    def __len__(self):
        size = 0
        current_node = self.head
        if self.head:
            size += 1
        while current_node.next and current_node.next != self.head:
            size += 1
            current_node = current_node.next

        return size

    def add_item(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if not self.head:
            self.head = item
       	    self.tail = item
            self.tail.next = self.head
        else:
            self.tail.next = item
            self.tail = item
            self.tail.next = self.head

    def is_circular(self):
        current_node = self.head
        if not self.head:
            return True
        hare = self.head
        tortoise = self.head
        while current_node.next and hare and tortoise:
            tortoise = tortoise.next
            hare = hare.next.next if hare.next else None
            if hare == tortoise:
                return True
            current_node = current_node.next
        return False


a = Node(1)
b = Node(2)
c = Node(3)

ll = CircularLinkedList()
#print(ll)
ll.add_item(a)
ll.add_item(b)
ll.add_item(c)
ll.add_item(10)
ll.add_item(50)
ll.add_item(60)


print(ll)

print(len(ll))

print(ll.is_circular())

