class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node()
        self.front = self.head
        self.rear = self.head

    def enqueue(self, data):
        new_node = Node(data)
        if self.front == None and self.rear == None:
            self.front = new_node
            self.rear = new_node
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            self.front = self.front.next

    def front_of_queue(self):
        if self.rear.data == None:
            print("Queue is Empty!")
        else:
            print(self.rear.data)

    def is_empty(self):
        if self.front.data == None and self.rear.data == None:
            return True
        else:
            return False

    def display_queue(self):
        queue = []
        current_node = self.front
        while current_node.next != None:
            current_node = current_node.next
            queue.append(current_node.data)
        print(queue)


haha = Queue()
haha.dequeue()
haha.dequeue()
haha.dequeue()
haha.enqueue(4)
haha.display_queue()
haha.front_of_queue()
