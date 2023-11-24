class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.tail
            self.tail.prev=new_node
            self.tail=new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dequeued_data=self.head.data
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.prev
                self.head.next=None
            return dequeued_data

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current_node=self.tail
            while current_node:
                print(current_node.data)
                current_node=current_node.next
