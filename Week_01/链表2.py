class Node:
    def __init__(self,data):
        self.node = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self,index):
        if index < 0 or index >= self.size:
            raise  Exception('超出链表节点范围')
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self,data,index):
        if index < 0 or index > self.size:
            raise Exception('超出链表节点范围')
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.last = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif self.size == index:
            self.last = node
            self.last.next = node
        else:
            prev_node = self.get(index-1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    


