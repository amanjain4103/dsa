class CircularQueue:

    def __init__(self, size):
        self.items = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return False

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.items[self.rear] = item
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None

        popped = self.items[self.front]
        self.items[self.front] = None 

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return popped

    def print_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        index = self.front
        while index != self.rear:
            print(self.items[index], end=" -> ")
            index = (index + 1) % self.size
        print(self.items[self.rear])