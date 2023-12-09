class Node:
    def __init__(self, data):
        self.data=data
        self.pref=None

class Stack:
    def __init__(self):
        self.end=None

    def push(self, val):
        new_node=Node(val)
        if self.end is None:
            self.end=new_node
        else:
            new_node.pref=self.end
            self.end=new_node

    def pop(self):
        if self.end is None:
            return None
        popped_val = self.end.data
        self.end = self.end.pref
        return popped_val

    def print(self):
        current=self.end
        while current:
            element_sep=' ' if current.pref is not None else '\n'
            print(current.data, end=element_sep)
            current=current.pref

stack=Stack()

stack.push(8)
stack.push(4)
stack.push(1)
stack.print()

print(stack.pop())
stack.print()