class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            del self.queue[0]

    def top(self):
        print(self.queue[-1])

    def is_empty(self):
        return self.queue == []

    def display_queue(self):
        print(self.queue)


haha = Queue()
haha.display_queue()
