from g4g_linkedList.Node import Node


class LinkedList:
    """docstring for LinkedList."""

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def printList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def deleteNodeByValue(self, key):
        temp = self.head
        if(self.head == None):
            return 
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return 
        while temp != None:
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        if(temp != None):
            prev.next = temp.next
            temp = None

    def push(self, data):
        new_node = Node(data)
        top = self.head
        new_node.next = top
        self.head = new_node

    def pop(self):
        temp = self.head
        if(self.head == None):
            return None
        if(temp.next != None):
            temp = temp.next
            self.head = temp
        return temp

    def insert(self, n, data):
        new_node = Node(data)
        temp = self.head
        if(n == 1):
            new_node = self.head
            self.head = new_node
            return
        for i in range (n - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def lengthByiteration(self):
        temp = self.head
        i = 0
        while(temp.next != None):
            temp = temp.next
            i += 1
        return i + 1

    def lengthByRecursion(self, node):
        if(not node):
            return 0
        return 1 + self.lengthByRecursion(node.next)

    def getLength(self):
        return self.lengthByRecursion(self.head)

    def createLoop(self):
        self.head.next.next.next.next = self.head.next
        return

    def detectLoop(self):
        flag = 0
        slow = self.head
        fast = self.head
        while(slow.data and fast.data and fast.next.data and fast.next.next.data):
            if(slow == fast and flag != 0):
                print('found')
                count = 1
                slow = slow.next
                while(slow != fast):
                    slow = slow.next
                    count += 1
                print(count) 
                return

            slow = slow.next
            fast = fast.next.next
            flag = 1
        print('not found')

'''
linkedList = LinkedList()
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
linkedList.insert(2, 55)
linkedList.printList()
print ('')
print('length by iteration: ', linkedList.lengthByiteration())
print('length by recurssion: ', linkedList.getLength())

linkedList.createLoop()
linkedList.detectLoop()
'''
