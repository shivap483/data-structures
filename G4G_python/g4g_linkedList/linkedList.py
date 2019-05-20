from Node import Node

class LinkedList:
    """docstring for LinkedList."""

    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_node=Node(data)
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=new_node
        print(current.data)

    def printList(self):
        node=self.head
        while node.next!=None:
            node=node.next
            print(node.data)

linkedList=LinkedList()
linkedList.append(9)
linkedList.append(4)
linkedList.append(12)
linkedList.append(0)
linkedList.append(5)
linkedList.append(34)
linkedList.printList()
