class Stack:
    def __init__(self):
        self.array = list()

    def push(self, el):
        self.array.append(el)

    def pop(self):
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0


class QueueFromStacks:
    def __init__(self):
        self.main_stack = Stack()
        self.other_stack = Stack()

    def enqueue(self, el):
        while not self.other_stack.is_empty():
            self.main_stack.push(self.other_stack.pop())
        self.main_stack.push(el)

    def dequeue(self):
        while not self.main_stack.is_empty():
            self.other_stack.push(self.main_stack.pop())
        return self.other_stack.pop()


if __name__ == '__main__':
    x = QueueFromStacks()
    x.enqueue(1)
    x.enqueue(2)
    x.enqueue(3)
    print(x.dequeue())
    print(x.dequeue())
    x.enqueue(4)
    print(x.dequeue())
    print(x.dequeue())

