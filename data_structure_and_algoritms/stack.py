

class Stack:
    """
    Stack implementation using list
    """
    def __init__(self, size):
        self.size = size
        self.array = []

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

    def push(self, value):
        if len(self.array) == self.size:
            print("Stack is already full")
        else:
            self.array.insert(0, value)

    def pop(self):
        if len(self.array) == 0:
            print("Stack is already empty")
        else:
            return self.array.pop(0)

    def peek(self):
        if len(self.array) == 0:
            print("Stack is already empty")
        return self.array[0]


stack = Stack(2)

print(stack)

stack.pop()

stack.push(10)
stack.push(20)
stack.push(30)
print(stack)


print(stack.pop())
print(stack)

print(stack.peek())
