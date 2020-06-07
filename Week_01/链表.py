class Node():
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return f'{self.item}==>{self.next}'

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def iternode(self):
        current = self.head
        while current:
            yield current
            current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    for i in ll.iternode():
        print(i)
