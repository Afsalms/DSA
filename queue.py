

class Queue:

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
            print("Queue is already full")
        else:
            self.array.append(value)


    def pop(self):
        if len(self.array) == 0:
            print("Queue is empty")
        else:
            return self.array.pop(0)


    def peek(self):
        if len(self.array) == 0:
            print("Queue is empty")
        else:
            return self.array[0]



queue = Queue(2)

print(queue)

queue.pop()

queue.push(10)
queue.push(20)
queue.push(30)
print(queue)


print(queue.pop())
print(queue)

print(queue.peek())

