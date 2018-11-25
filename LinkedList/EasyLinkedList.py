class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elements = []

    def add(self, data):
        new_node = Node(data)  # 5, 4
        if self.tail:
            self.tail.next = new_node  # 4
            self.tail = new_node  # 4
            self.elements.append(self.tail.data)
        else:
            self.tail = new_node  # 5
            self.head = new_node  # 5
            self.elements.append(self.head.data)
        print(self.elements)


myList = LinkedList()
myList.add(5)
myList.add(4)
