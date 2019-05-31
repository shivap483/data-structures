'''
Created on 31-May-2019

@author: shiva
'''
from g4g_linkedList.Node import Node


class Stack:

    def __init__(self):
        self.top = None
    
    def push(self, data):
        if(self.top == None):
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        
    def pop(self):
        if(self.top == None):
            print('empty stack')
            return
        else:
            x = self.top
            self.top = self.top.next
            x.next = None
            print('popped element: ', x.data)
            return x
    
    def peek(self):
        if(self.top == None):
            print('empty stack')
            return
        else:
            print(self.top.data)
            return self.top.data
        
        
s = Stack()
s.pop()
s.peek()
s.push(3)
s.push(6)
s.push(4)
s.peek()
s.pop()
s.peek()

