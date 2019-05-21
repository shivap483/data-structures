from Node import Node

class LinkedList:
    """docstring for LinkedList."""

    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_node=Node(data)
        current=self.head

        while current!=None:
            current=current.next
        current=new_node
        #print(current.data)

    def printList(self):
        node=self.head
        while node!=None:
            print(node.data)
            node=node.next


    def deleteNodeByValue(self, data):
        node=self.head
        if(node.data==data):
            node=node.next
            return
        while node.next!=None:
            temp=node.next
            if(temp.data==data):
                node.next=temp.next
                break
            node=node.next


linkedList=LinkedList()
linkedList.append(9)
linkedList.append(4)
linkedList.append(12)
linkedList.append(0)
linkedList.append(5)
linkedList.append(34)
linkedList.printList()
#linkedList.deleteNodeByValue(5)
#linkedList.printList()
