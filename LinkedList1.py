'''

Linked List 1

Author : Karthik Goudar
date   : 30 JAN, 2023

'''


# creating a Node
class Node():
    def __init__(self, data):
        self.data = data
        self.node = None


# creating a Linked-List
class LinkedList(Node):
    def __init__(self):
        self.head = None

    def Print_LL(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            print(n)
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    # Adding elements at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # adding elements at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node




LL1 = LinkedList()
LL1.add_begin(120)
Ll1.add_begin(159)
LL1.add_end(200)
LL1.Print_LL()
