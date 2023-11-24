class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.end=None

    def push(self, data):
        new_node=Node(data)
        if self.end is None:
            self.end=new_node
        else:
            new_node.next=self.end
            self.end=new_node

    def pop(self):
        if self.end is None:
            return None
        popped_data = self.end.data
        self.end = self.end.next
        return popped_data

    def print_stack(self):
        current=self.end
        while current:
            element_sep=' ' if current.next is not None else '\n'
            print(current.data, end=element_sep)
            current=current.next

stack=Stack()

stack.push(8)
stack.push(4)
stack.push(1)
stack.print_stack()

print(stack.pop())
stack.print_stack()