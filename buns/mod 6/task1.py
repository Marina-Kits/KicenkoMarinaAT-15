class Node:
    def __init__(self, data):
        self.data=data
        self.nref=None

class LinkedList:
    def __init__(self):
        self.start=None

    def push(self, val):
        new_node=Node(val)
        if self.start is None:
            self.start=new_node
        else:
            current=self.start
            while current.nref is not None:
                current=current.nref
            current.nref=new_node

    def get(self, index):
        if index<0:
            return None
        current=self.start
        count=0
        while current is not None:
            if count==index:
                return current.data
            current=current.nref
            count+=1
        return None

    def remove(self, index):
        if index<0:
            return None
        if index==0:
            self.start=self.start.nref
            return
        current=self.start
        prev=None
        count=0
        while current is not None:
            if count==index:
                prev.nref=current.nref
                return
            prev=current
            current=current.nref
            count+=1
        return None

    def insert(self, n, val):
        new_node=Node(val)
        if n==0:
            new_node.nref=self.start
            self.start=new_node
        else:
            current=self.start
            count=0
            while current is not None:
                if count==n-1:
                    new_node.nref=current.nref
                    current.nref=new_node
                    return
                current=current.nref
                count+=1
            return None

    def __iter__(self):
        current=self.start
        while current is not None:
            yield current.data
            current=current.nref

linked_list=LinkedList()
linked_list.push(8)
linked_list.push(9)
linked_list.push(7)

print(list(linked_list))

print(linked_list.get(1))
print(linked_list.get(3))
print(linked_list.get(-2))

linked_list.remove(1)
print(list(linked_list))

linked_list.insert(1, 5)
print(list(linked_list))
