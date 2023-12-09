class Node:
    def __init__(self, data):
        self.data=data
        self.nref=None
        self.pref=None

class Queue:
    def __init__(self):
        self.start=None
        self.end=None

    def push(self, val):
        new_val=Node(val)
        if self.start is None:
            self.start=new_val
            self.end=new_val
        else:
            new_val.pref=self.end
            new_val.nref=None
            self.end.nref=new_val
            self.end=new_val

    def pop(self):
        if self.start is None:
            return None
        else:
            val=self.start
            self.start=self.start.nref
            if self.start is not None:
                self.start.pref=None
            else:
                self.end=None
            return val.data

    def insert(self, n, val):
        new_val=Node(val)
        if n==0:
            new_val.nref=self.start
            self.start.prev=new_val
            self.start=new_val
        else:
            current=self.start
            for i in range(n):
                if current.nref is None:
                    print("Position out of range")
                    return
                current=current.nref
            new_val.pref=current.pref
            new_val.nref=current
            current.pref.nref=new_val
            current.pref=new_val

    def print(self):
        current=self.start
        while current:
            separator=' ' if current.nref is not None else '\n'
            print(current.data, end=separator)
            current=current.nref

queue=Queue()

queue.push(1)
queue.push(3)
queue.push(5)
queue.push(7)
queue.push(9)
queue.print()

print(queue.pop())
queue.print()

queue.insert(3,1)
queue.print()