from _ast import If


class stack():

    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        if(self.top == len(self.stack) - 1):
            print('sack overflow')
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if(self.top == -1):
            print('empty stack')
            return
        x = self.stack[self.top]
        self.top -= 1
        print(x)
        return x
    
    def peek(self):
        if (self.top == -1):
            print('empty stack')
            return
        print(self.stack[self.top])
        return self.stack[self.top]

        
s = stack(10)
s.push(1)
s.peek()
s.pop()
s.peek()
