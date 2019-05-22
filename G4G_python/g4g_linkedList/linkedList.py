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

    def printList(self):
        node=self.head
        while node.next!=None:
            node=node.next
            print(node.data)


    def deleteNodeByValue(self, data):
        node=self.head
        while node.next!=None:
            temp=node.next
            if(temp.data==data):
                node.next=temp.next
                break
            node=node.next


    def push(self,data):
        new_node=Node(data)
        head=self.head
        new_node.next=head.next
        head.next=new_node

    def pop(self):
        temp=self.head
        if(temp.next!=None):
            temp=temp.next
            self.head.next=temp.next
        return temp

    def insert(self,i,data):
        new_node=Node(data)
        temp=self.head
        j=1
        while(i!=j and temp.next!=None):
            temp=temp.next
            j+=1
        temp=new_node

linkedList=LinkedList()
linkedList.pop()
linkedList.append(9)
linkedList.append(4)
linkedList.append(12)
linkedList.append(0)
linkedList.append(5)
linkedList.append(34)
linkedList.printList()
print ('')
linkedList.deleteNodeByValue(5)
linkedList.push(22)
linkedList.push(8)
linkedList.printList()
print ('')
linkedList.pop()
linkedList.printList()
print ('')
print(linkedList.pop().data)
print ('')
linkedList.insert(1,55)
linkedList.printList()
print ('')


