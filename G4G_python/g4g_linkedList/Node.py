'''
Created on 11-Apr-2019

@author: shiva
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

        
class LinkedList:

    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
llist.head.next = second
second.next = third
llist.printList()

