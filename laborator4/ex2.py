class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())  # 1
print(queue.peek())  # 2
print(queue.pop())  # 2
print(queue.peek())  # 3
print(queue.pop())  # 3
print(queue.pop())  # None