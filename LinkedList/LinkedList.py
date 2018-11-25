class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        number_of_elements = 0
        current_node = self.head
        while current_node.next != None:
            number_of_elements += 1
            current_node = current_node.next
        return number_of_elements

    def display_list(self):
        elements = ""
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements += str(current_node.data)
        print(elements)


my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(6)
my_list.add(7)
my_list.display_list()
print(my_list.length())

# def remove(self):
#     current_node = self.head
#     new_node = current_node
#     while current_node.next != None:
#         current_node = current_node.next
#     current_node = current_node.next
