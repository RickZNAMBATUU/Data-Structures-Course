class Stacks:
    def __init__(self):
        self.my_stacks = []

    def push(self, item):
        self.my_stacks.append(item)

    def pop(self):
        if self.my_stacks:
            item_popped = self.my_stacks[-1]
            del self.my_stacks[-1]
            return item_popped
        else:
            print("Empty Stacks")

    def top(self):
        return self.my_stacks[-1]

    def is_empty(self):
        return self.my_stacks == []

    def display_stacks(self):
        return self.my_stacks


if __name__ == "__main__":
    my_stack = Stacks()
